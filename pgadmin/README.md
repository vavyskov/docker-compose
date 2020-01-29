# pgAdmin

## Requirements:
- docker
- docker-compose

## Quick Start
- Clone or download this repository
- Go inside of directory, `cd docker-compose-pgadmin`
- Run command `docker-compose up -d`

## Environments
This Compose file contains the following environment variables:

- `PGADMIN_VERSION` the default value is **latest**
- `PGADMIN_PORT` the default value is **5050**
- `PGADMIN_DEFAULT_EMAIL` the default value is **pgadmin@pgadmin.org**
- `PGADMIN_DEFAULT_PASSWORD` the default value is **pgadmin**

## Access to PgAdmin: 
- **URL:** `http://localhost:5050`
- **Username:** pgadmin@pgadmin.org (as a default)
- **Password:** pgadmin (as a default)

## Add a new server in PgAdmin:
- **Host name/address** `postgres`
- **Port** `5432`
- **Username** as `POSTGRES_USER`, by default: `postgres`
- **Password** as `POSTGRES_PASSWORD`, by default `postgres`

## Note
- stop this service: `docker-compose stop`
- start this service: `docker-compose start`
- delete this service: `docker-compose down`
- delete docker volume: `docker volume prune`
