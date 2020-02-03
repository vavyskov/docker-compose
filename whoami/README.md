# Whoami

## Requirements:
1. [Docker CE](https://download.docker.com?target=_blank) or [Docker Toolbox](https://github.com/docker/toolbox/releases/?target=_blank) (Virtualbox)
    - `docker`
    - `docker-compose`
1. [Git](https://git-scm.com/?target=_blank) (optional)
    - `git`

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

          docker network create frontend_network; \
          docker-compose up -d

    - Docker Swarm

          docker network create --driver=overlay frontend_network; \
          docker stack deploy --compose-file=docker-compose.yml whoami

## Quick start (docker)
    docker network create frontend_network; \
    docker run -itd \
        --name whoami \
        --publish 8082:80 \
        --network frontend_network \
        containous/whoami:v1.4.0

## Network
Show IP address:

    docker network inspect frontend_network | grep IPv