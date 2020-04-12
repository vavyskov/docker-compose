# Traefik

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

          docker-compose up -d

    - Docker Swarm

          docker stack deploy --compose-file=docker-compose.yml traefik

## Quick start (docker)

    docker network create -d overlay --attachable frontend_network; \
    docker run -itd \
        --name traefik \
        --publish 80:80 \
        --publish 443:443 \
        --publish 8080:8080 \
        --network frontend_network \
        traefik:2.1
        
## Access to Traefik: 
- **URL:** `http://localhost:8080` (Docker Toolbox: `192.168.99.100:8080`)
- **User:** `traefik`
- **Password:** `traefik`

## Network
Show IP address:

    docker network inspect frontend_network | grep IPv

## Let's Encrypt
[Traefik - Let's Encrypt](https://git-scm.com/?target=_blank)

## Custom certificates

Dynamic folder with `certificates.yml` file is the only available method to configure custom certificates!