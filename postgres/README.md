# Postgres

## Environments
This Compose file contains the following environment variables:

- `POSTGRES_VERSION` the default value is **12**
- `POSTGRES_PORT` the default value is **5432**
- `POSTGRES_USER` the default value is **postgres**
- `POSTGRES_PASSWORD` the default value is **postgres**

You can set environment variables in `.env` file.

## Quick start (docker-compose)
1. Clone or download this repository
1. Go inside of directory `cd docker-compose/postgres`
1. Run command:
    - Docker:

          docker-compose up -d

    - Docker Swarm

          docker stack deploy --compose-file=docker-compose.yml postgres

## Quick start (docker)

    docker volume create --name postgres_data; \
    docker network create -d overlay --attachable backend_network; \
    docker run -itd \
        --name postgres \
        --env POSTGRES_USER=postgres \
        --env POSTGRES_PASSWORD=postgres \
        --volume postgres_data:/var/lib/postgresql/data \
        --publish 5432:5432 \
        --network frontend_network \
        --restart unless-stopped \
        postgres:12

## Access to Postgres
- **URL:** `localhost:5432` (Docker Toolbox: `192.168.99.100:5432`)
- **Username:** `postgres`
- **Password:** `postgres`

## Network
Show IP address:

    docker network inspect backend_network | grep IPv
