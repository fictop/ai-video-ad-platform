# Use a lightweight base image
FROM python:3.10-alpine as builder

# Set the working directory
WORKDIR /app

# Install system dependencies
RUN apk add --no-cache gcc musl-dev python3-dev libffi-dev

# Install dependencies in a virtual environment
COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# Second stage: create a minimal final image
FROM python:3.10-alpine

# Set the working directory
WORKDIR /app

# Copy only necessary files from the builder stage
COPY --from=builder /install /usr/local
COPY . /app

# Expose the port
EXPOSE 8000

# Run the application
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:8000"]
