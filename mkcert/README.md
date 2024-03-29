# mkcert

A fast and simple way to generate CA and SSL certificates for your local dev environment.

## Environments
This Compose file contains the following environment variables:

- `MKCERT_HOSTNAMES` the default value is **\*.localhost.dev \*.localhost.test \*.example.com \*.example.edu**
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

    docker run --rm -v $PWD/certificates:/root/.local/share/mkcert vavyskov/mkcert:1.4.3-1.1.0

    docker run --rm \
        -v $PWD/certificates:/root/.local/share/mkcert \
        -e MKCERT_HOSTNAMES="*.local *.example.com" \
        -e HOST_USER_ID="1000" \
        -e HOST_USER_NAME="user" \
        vavyskov/mkcert:1.4.3-1.1.0

## Adding trusted root certificate authority
1. Operating system
   - **Linux (Debian)**:

         sudo cp rootCA.crt /usr/local/share/ca-certificates/
         sudo update-ca-certificates

2. Browsers:
   - **Chrome**: Settings -> Privacy and security -> Security -> Manage certificates -> Authorities -> Import (rootCA.crt)
