FROM python:3.10-slim
WORKDIR /app

# Upgrade pip first
RUN pip install --upgrade pip

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:7860"]
