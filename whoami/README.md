# Whoami

## Environments
This Compose file contains the following environment variables:

- `WHOAMI_VERSION` the default value is **v1.4.0**
- `WHOAMI_PORT` the default value is **8082**

You can set environment variables in `.env` file.

## Quick start (docker-compose)
1. Clone or download this repository
1. Go inside of directory `cd docker-compose/whoami`
1. Run command:
    - Docker:

          docker network create frontend_network
          (docker network create --attachable frontend_network)
          docker-compose up -d
          
          docker-compose -f whoami2.yml up -d
          docker-compose -f whoami3.yml up -d

    - Docker Swarm

          docker network create --driver=overlay frontend_network
          (docker network create --driver=overlay --attachable frontend_network)
          docker stack deploy --compose-file=docker-compose.yml whoami

## Quick start (docker)
    docker network create -d overlay --attachable frontend_network; \
    docker run -itd \
        --name whoami \
        --publish 8082:80 \
        --network frontend_network \
        containous/whoami:v1.4.0

## Access to Whoami: 
- **URL:** `http://localhost:8082` (Docker Toolbox: `192.168.99.100:8082`)

## Network
Show IP address:

    docker network inspect frontend_network | grep IPv