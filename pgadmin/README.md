# pgAdmin

## Requirements:
1. [Docker CE](https://download.docker.com?target=_blank) or [Docker Toolbox](https://github.com/docker/toolbox/releases/?target=_blank) (Virtualbox)
    - `docker`
    - `docker-compose`
1. [Git](https://git-scm.com/?target=_blank) (optional)
    - `git`

## Environments
This Compose file contains the following environment variables:

- `PGADMIN_VERSION` the default value is **4**
- `PGADMIN_PORT` the default value is **5050**
- `PGADMIN_DEFAULT_EMAIL` the default value is **pgadmin<span>@</span>pgadmin<span>.</span>org**
- `PGADMIN_DEFAULT_PASSWORD` the default value is **pgadmin**

You can set environment variables in `.env` file.

## Quick start (docker-compose)
1. Clone or download this repository
1. Go inside of directory `cd docker-compose/pgadmin`
1. Run command:
    - Docker:

          docker network create backend_network; \
          docker network create frontend_network; \
          docker-compose up -d

    - Docker Swarm

          docker network create --driver=overlay backend_network; \
          docker network create --driver=overlay frontend_network; \
          docker stack deploy --compose-file=docker-compose.yml pgadmin

## Quick start (docker)

    docker volume create --name pgadmin_data; \
    docker network create backend_network; \
    docker network create frontend_network; \
    docker run -itd \
        --name pgadmin \
        --env PGADMIN_DEFAULT_EMAIL=pgadmin@pgadmin.org \
        --env PGADMIN_DEFAULT_PASSWORD=pgadmin \
        --volume pgadmin_data:/var/lib/pgadmin \
        --publish 5050:80 \
        --network frontend_network \
        --restart unless-stopped \
        dpage/pgadmin4:4
        
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
        
## Network
Show IP address:

    docker network inspect backend_network | grep IPv
    docker network inspect frontend_network | grep IPv