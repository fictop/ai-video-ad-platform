# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Upgrade pip and install dependencies from requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run the Flask app using gunicorn on port 8000
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:8000"]
