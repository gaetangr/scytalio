# Use the official Python image as a base image for the backend
FROM python:3.11-slim AS backend

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Use the official Node.js image as a base image for the frontend
FROM node:18 AS frontend

# Set the working directory in the container
WORKDIR /frontend

# Copy the package.json and package-lock.json files into the container
COPY frontend/package.json frontend/package-lock.json ./

# Install the dependencies
RUN npm install

# Copy the rest of the frontend code into the container
COPY frontend .

# Build the frontend
RUN npm run build

# Use the official Python image as a base image for the final image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the backend and frontend build artifacts into the final image
COPY --from=backend /app /app
COPY --from=frontend /frontend/dist /app/frontend/dist

# Expose the port the app runs on
EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
