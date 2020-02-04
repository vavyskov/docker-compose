# Traefik

## Requirements:
1. [Docker CE](https://download.docker.com?target=_blank) or [Docker Toolbox](https://github.com/docker/toolbox/releases/?target=_blank) (Virtualbox)
    - `docker`
    - `docker-compose`
1. [Git](https://git-scm.com/?target=_blank) (optional)
    - `git`

## Environments
This Compose file contains the following environment variables:

- `TRAEFIK_VERSION` the default value is **2.1**
- `TRAEFIK_PORT` the default value is **8080**

You can set environment variables in `.env` file.

## Quick start (docker-compose)
1. Clone or download this repository
1. Go inside of directory `cd docker-compose/traefik`
1. Run command:
    - Docker:

          docker network create frontend_network; \
          docker-compose up -d

    - Docker Swarm

          docker network create --driver=overlay frontend_network; \
          docker stack deploy --compose-file=docker-compose.yml traefik

## Quick start (docker)

    docker network create frontend_network; \
    docker run -itd \
        --name traefik \
        --publish 80:80 \
        --publish 443:443 \
        --publish 8080:8080 \
        --network frontend_network \
        traefik:2.1
        
## Access to Traefik: 
- **URL:** `http://localhost:8080` (Docker Tools: `192.168.99.100:8080`)
- **User:** `test`
- **Password:** `test`

## Network
Show IP address:

    docker network inspect frontend_network | grep IPv

## Let's Encrypt
[Traefik - Let's Encrypt](https://git-scm.com/?target=_blank)
