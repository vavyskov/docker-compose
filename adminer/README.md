# Adminer

## Environments
This Compose file contains the following environment variables:

- `ADMINER_VERSION` the default value is **4**
- `ADMINER_PORT` the default value is **8081**

You can set environment variables in `.env` file.

## Quick start (docker-compose)
1. Clone or download this repository
1. Go inside of directory `cd docker-compose/adminer`
1. Run command:
    - Docker:

          docker network create frontend_network
          docker network create database_network
          docker-compose up -d

    - Docker Swarm

          docker network create --driver=overlay frontend_network
          docker network create --driver=overlay database_network
          docker stack deploy --compose-file=docker-compose.yml adminer

## Quick start (docker)

    docker network create -d overlay --attachable frontend_network; \
    docker network create -d overlay --attachable database_network; \
    docker run -itd \
        --name adminer \
        --publish 8081:80 \
        --network frontend_network \
        adminer:4

## Access to Adminer: 
- **URL:** `http://localhost:8081` (Docker Toolbox: `192.168.99.100:8081`)

## Network
Show IP address:

    docker network inspect frontend_network | grep IPv
    docker network inspect database_network | grep IPv
