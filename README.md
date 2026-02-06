# Bike Sharing Platform — Assignment Service

Production-style microservice for temporary bike assignments.

## Why DDD
Domain rules are isolated in the Core Domain.
The API is a thin adapter.

## Architecture
- domain
- application
- infrastructure
- api
- docker-compose

## Run
docker compose -p bike-sharing up --build -d

## Demo
./scripts/demo.sh <EC2_PUBLIC_IP>
