# Dockerfile for backend
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN apt-get update && apt-get install -y nginx

COPY nginx.conf /etc/nginx/nginx.conf

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
