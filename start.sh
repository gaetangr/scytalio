#!/bin/bash
cd /frontend && npm run dev -- --host 0.0.0.0 &

cd /app && uvicorn main:app --host 0.0.0.0 --port 8000
