FROM node:18-slim AS frontend-builder
WORKDIR /frontend
COPY frontend/package*.json ./
RUN npm install --no-cache
COPY frontend/ .
ENV VITE_HOST=0.0.0.0
RUN npm run build

FROM python:3.13-slim
WORKDIR /app
RUN apt-get update && \
    apt-get install -y nodejs npm && \
    rm -rf /var/lib/apt/lists/*

COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ .
COPY --from=frontend-builder /frontend /frontend

EXPOSE 5173 8000

LABEL maintainer="scytalio@mail.gaetangrond.me" \
      version="1.0.0" \
      description="Scytalio is an open-source API designed for storing and retrieving encrypted messages"

LABEL org.opencontainers.image.source="https://github.com/gaetangr/scytalio"
LABEL org.opencontainers.image.description="Scytalio is an open-source API designed for storing and retrieving encrypted messages"
LABEL org.opencontainers.image.licenses="MIT"

CMD sh -c "cd /frontend && npm run dev -- --host 0.0.0.0 & cd /app && uvicorn main:app --host 0.0.0.0 --port 8000"