# Traefik

## Environments
This Compose file contains the following environment variables:

- `COMPOSE_PROJECT_NAME` the default value is **traefik**
- `MKCERT_VERSION` the default value is **1.4.3-alpine3.13**
- `SERVER_HOSTNAMES` the default value is **\*.localhost.dev \*.localhost.test \*.example.com \*.example.edu**
- `HOST_USER_ID` the default value is **1000**
- `HOST_USER_NAME` the default value is **user**
- `TRAEFIK_VERSION` the default value is **v2.5**
- `TRAEFIK_PORT` the default value is **8080**

You can set environment variables in `.env` file.

## Quick start (docker-compose)
1. Clone or download this repository
1. Go inside of directory `cd docker-compose/traefik`
1. Run command:
    - Docker:

          docker network create frontend_network
          docker-compose up -d

    - Docker Swarm

          docker network create --driver=overlay frontend_network
          docker stack deploy --compose-file=docker-compose.yml traefik
          docker stack deploy --compose-file=docker-compose.override.yml traefik

## Quick start (docker)

    docker network create frontend_network; \
    docker run --rm -v $PWD/certificates:/root/.local/share/mkcert vavyskov/mkcert:1.4.3-alpine3.13; \
    docker run -itd \
        --name traefik \
        --publish 80:80 \
        --publish 443:443 \
        --publish 8080:8080 \
        --network frontend_network \
        traefik:v2.5
        
## Access to Traefik: 
- **URL:** `http://localhost:8080` (Docker Toolbox: `192.168.99.100:8080`)
- **User:** `traefik`
- **Password:** `traefik`

## Adding trusted root certificate authority
1. Operating system
   - **Linux (Debian)**:

         sudo cp rootCA.pem /usr/local/share/ca-certificates/
         sudo update-ca-certificates

2. Browsers:
   - **Chrome**: Settings -> Privacy and security -> Security -> Manage certificates -> Authorities -> Import (rootCA.pem)

## Custom certificates

Config folder with `dynamic.yml` file is the only available method to configure custom certificates!

## Network
Show IP address:

    docker network inspect frontend_network | grep IPv

## Let's Encrypt
[Traefik - Let's Encrypt](https://git-scm.com/?target=_blank)
