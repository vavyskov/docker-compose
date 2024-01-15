# Nginx-proxy

## Environments
This Compose file contains the following environment variables:

- `COMPOSE_PROJECT_NAME` the default value is **nginx-proxy**
- `NGINX_PROXY_VERSION` the default value is **0.9-alpine**

You can set environment variables in `.env` file.

## Quick start (docker-compose)
1. Clone or download this repository
1. Go inside of directory `cd docker-compose/nginx-proxy`
1. Run command:
    - Docker:

          docker network create frontend_network
          docker-compose up -d

    - Docker Swarm

          docker network create --driver=overlay frontend_network
          docker stack deploy --compose-file=docker-compose.yml nginx-proxy

## Container behind Nginx-proxy require environment settings

HTTP:

    ...
      environment:
        ## Nginx-proxy
        - VIRTUAL_HOST=project.example.com
    ...

HTTPS:

    ...
      environment:
        ## Nginx-proxy
        - VIRTUAL_HOST=project.example.com
        - VIRTUAL_PORT=443
        - VIRTUAL_PROTO=https
    ...

## Certificates

A container with `VIRTUAL_HOST=project.example.com` should have a `project.example.com.crt` and `project.example.com.key` file in the `../mkcert/certificates` directory.

**Wildcard certificates** example `VIRTUAL_HOST=project.example.com` would use certificate name `example.com.crt` and `example.com.key`.
