# pgAdmin

## Requirements:
1. [Docker CE](https://download.docker.com?target=_blank) or [Docker Toolbox](https://github.com/docker/toolbox/releases/?target=_blank) (Virtualbox)
    - `docker`
    - `docker-compose`
1. [Git](https://git-scm.com/?target=_blank) (optional)
    - `git`

## Quick Start
- Clone or download this repository
- Go inside of directory, `cd docker-compose/pgadmin`
- Run command `docker-compose up -d`

## Environments
This Compose file contains the following environment variables:

- `PGADMIN_VERSION` the default value is **latest**
- `PGADMIN_PORT` the default value is **5050**
- `PGADMIN_DEFAULT_EMAIL` the default value is **pgadmin<span>@</span>pgadmin<span>.</span>org**
- `PGADMIN_DEFAULT_PASSWORD` the default value is **pgadmin**

You can set environment variables in `.env` file.

## Access to PgAdmin: 
- **URL:** `http://localhost:5050` (Docker Tools: `192.168.99.100:5050`)
- **Username:** `pgadmin@pgadmin.org`
- **Password:** `pgadmin`

## Add a new server in PgAdmin:
**Menu:** Object -> Create -> Server
- **General** tab:
  - **Name:** MyCustomServerName
- **Connection** tab:
  - **Host name/address:** `postgres` (Docker Tools: `192.168.99.100`)
  - **Port:** `5432`
  - **Username:** `postgres`
  - **Password:** `postgres`

## Note
- Stop this service: `docker-compose stop`
- Start this service: `docker-compose start`
- Delete this service: `docker-compose down`
- Delete docker volume: `docker volume prune`

## Terminal
    docker volume create --name pgadmin; \
    docker network create --driver bridge backend; \
    docker run -itd \
        --name pgadmin \
        --env PGADMIN_DEFAULT_EMAIL=pgadmin@pgadmin.org \
        --env PGADMIN_DEFAULT_PASSWORD=pgadmin \
        --volume pgadmin:/var/lib/pgadmin \
        --publish 5050:80 \
        --network backend \
        --restart unless-stopped \
        dpage/pgadmin4:latest