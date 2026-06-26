FROM python:3.10-slim

WORKDIR /app

# Force Docker to break the cache and install Flask
RUN apt-get update && pip install --no-cache-dir flask

COPY . .

EXPOSE 5000

CMD ["python", "server.py"]
