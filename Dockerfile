# Use a minimal base image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt requirements.txt

# Install dependencies with optimizations
RUN pip install --no-cache-dir -r requirements.txt && \
    pip cache purge  # Remove extra files

# Copy the rest of the app
COPY . .

# Expose port 8000
EXPOSE 8000

# Run the application
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:8000"]
