#!/bin/bash

# Build Docker image
docker build -t kali-linux-online .

# Create Docker network
docker network create kali-network || true

# Run Flask application
docker run -d \
    --name kali-online-app \
    --network kali-network \
    -p 5000:5000 \
    -v /var/run/docker.sock:/var/run/docker.sock \
    -e DOCKER_HOST=unix:///var/run/docker.sock \
    kali-linux-online python3 app.py

echo "Kali Linux Online is running on http://localhost:5000"