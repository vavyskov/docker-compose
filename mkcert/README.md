# mkcert

A fast and simple way to generate CA and SSL certificates for your local dev environment.

## Environments
This Compose file contains the following environment variables:

- `SERVER_HOSTNAMES` the default value is **\*.localhost.dev \*.localhost.test \*.example.com \*.example.edu**
- `HOST_USER_ID` the default value is **1000**
- `HOST_USER_NAME` the default value is **user**

You can set environment variables in `.env` file.

## Quick start (docker-compose)
1. Clone or download this repository
1. Go inside of directory `cd docker-compose/mkcert`
1. Run command:
    - Docker:
    
          docker-compose up -d

    - Docker Swarm

          docker stack deploy --compose-file=docker-compose.yml mkcert

## Quick start (docker)

    docker run --rm -v $PWD:/root/.local/share/mkcert vavyskov/mkcert:1.4.3-alpine3.13

    docker run --rm \
        -v $PWD:/root/.local/share/mkcert \
        -e SERVER_HOSTNAMES="*.local *.example.com" \
        -e HOST_USER_ID="1000" \
        -e HOST_USER_NAME="user" \
        vavyskov/mkcert:1.4.3-alpine3.13
