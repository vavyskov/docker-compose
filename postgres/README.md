# PostgreSQL

## Requirements:
- docker
- docker-compose

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

## Access to postgres
- `localhost:5432`
- **Username:** postgres (as a default)
- **Password:** postgres (as a default)

## Connect to postgres
- host is to enter by `docker network inspect pgv_default` to check `postgres_container Ipv4`

## Note
- stop this service: `docker-compose stop`
- start this service: `docker-compose start`
- delete this service: `docker-compose down`
- delete docker volume: `docker volume prune`
