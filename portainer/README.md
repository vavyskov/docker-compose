# Portainer

## Environments
This Compose file contains the following environment variables:

- `AGENT_VERSION` the default value is **1.5.1**
- `PORTAINER_VERSION` the default value is **1.23.0**
- `PORTAINER_PORT` the default value is **9002**

You can set environment variables in `.env` file.

## Quick start (docker-compose)
1. Clone or download this repository
1. Go inside of directory `cd docker-compose/portainer`
1. Run command:
    - Docker Swarm (only)

          docker network create --driver=overlay backend_network; \
          docker network create --driver=overlay frontend_network; \
          docker stack deploy --compose-file=docker-compose.yml portainer

## Quick start (docker)

    docker volume create portainer_data; \
    docker network create -d overlay --attachable backend_network; \
    docker network create -d overlay --attachable frontend_network; \
    docker run -d \ 
        --name portainer \
        --publish 8000:8000 \
        --publish 9002:9000 \
        --restart always \
        --volume /var/run/docker.sock:/var/run/docker.sock \
        --volume portainer_data:/data \
        portainer/portainer:1.23.0

## Access to Portainer: 
- **URL:** `http://localhost:9002` (Docker Toolbox: `192.168.99.100:9002`)
        
## Network
Show IP address:

    docker network inspect agent_network | grep IPv
    docker network inspect frontend_network | grep IPv
