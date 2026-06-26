# ==========================================
# 1. BASE IMAGE & ENVIRONMENT SETUP
# ==========================================
# Use the official lightweight Python image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Prevent Python from writing .pyc files to disk
ENV PYTHONDONTWRITEBYTECODE=1

# Prevent Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED=1

# Upgrade pip inside the base image
RUN pip install --no-cache-dir --upgrade pip

# ==========================================
# 2. SOURCE CODE COPIER & NETWORKING
# ==========================================
# Copy all project files and scripts into the container
COPY . .

# Expose port 5000 for the Flask server
EXPOSE 5000

# ==========================================
# 3. DEFAULT CONTAINER EXECUTION
# ==========================================
# Execute the web server
CMD ["python", "server.py"]
