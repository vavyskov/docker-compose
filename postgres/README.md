# Postgres

## Requirements:
1. [Docker CE](https://download.docker.com?target=_blank) or [Docker Toolbox](https://github.com/docker/toolbox/releases/?target=_blank) (Virtualbox)
    - `docker`
    - `docker-compose`
1. [Git](https://git-scm.com/?target=_blank) (optional)
    - `git`

## Quick Start
- Clone or download this repository
- Go inside of directory, `cd docker-compose/postgres`
- Run command `docker-compose up -d`

## Environments
This Compose file contains the following environment variables:

- `POSTGRES_VERSION` the default value is **latest**
- `POSTGRES_USER` the default value is **postgres**
- `POSTGRES_PASSWORD` the default value is **postgres**

You can set environment variables in `.env` file.

## Access to Postgres
- **URL:** `localhost:5432` (Docker Tools: `192.168.99.100:5432`)
- **Username:** `postgres`
- **Password:** `postgres`

## Network
- Show IP address: `docker network inspect frontend | grep IPv`

## Note
- Stop this service: `docker-compose stop`
- Start this service: `docker-compose start`
- Delete this service: `docker-compose down`
- Delete docker volume: `docker volume prune`

## Terminal

### Docker
    docker volume create --name postgres; \
    docker network create frontend; \
    docker run -itd \
        --name postgres \
        --env POSTGRES_USER=postgres \
        --env POSTGRES_PASSWORD=postgres \
        --volume postgres:/var/lib/postgresql/data \
        --publish 5432:5432 \
        --network frontend \
        --restart unless-stopped \
        postgres:latest
        
### Docker Swarm
    docker network create --driver=overlay frontend; \
    docker stack deploy -c docker-compose.yml postgres