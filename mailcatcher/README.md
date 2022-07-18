# Mailcatcher

## Environments
This Compose file contains the following environment variables:

- `MAILCATCHER_VERSION` the default value is **alpine3.11**
- `COMPOSE_PROJECT_NAME` the default value is **mailcatcher**
- `MAILCATCHER_PORT` the default value is **1081**
- `SMTP_PORT` the default value is **1025**

You can set environment variables in `.env` file.

## Quick start (docker-compose)
1. Clone or download this repository
1. Go inside of directory `cd docker-compose/mailcatcher`
1. Run command:
    - Docker:

          docker network create frontend_network
          docker network create mailcatcher_network
          docker-compose up -d

    - Docker Swarm

          docker network create --driver=overlay frontend_network
          docker network create --driver=overlay mailcatcher_network
          docker stack deploy --compose-file=docker-compose.yml mailcatcher

## Quick start (docker)

    docker network create -d overlay --attachable frontend_network; \
    docker network create -d overlay --attachable mailcatcher_network; \
    docker run -itd \
        --name mailcatcher \
        --publish 1081:80 \
        --publish 1025:25 \
        --network frontend_network \
        vavyskov/mailcatcher:alpine3.11

## Access to Mailcatcher: 
- **URL:** `http://localhost:1081` (Docker Toolbox: `192.168.99.100:1081`)

## Network
Show IP address:

    docker network inspect frontend_network | grep IPv
    docker network inspect mailcatcher_network | grep IPv
