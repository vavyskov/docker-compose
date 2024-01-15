# httpd-proxy

## Environments
This Compose file contains the following environment variables:

- `COMPOSE_PROJECT_NAME` the default value is **httpd-proxy**
- `PROJECT_HOSTNAME` the default value is **app.example.com**
- `HTTPD_PROXY_VERSION` the default value is **2.4-1.0.0**

You can set environment variables in `.env` file.

## Configuration
```
sudo vim /etc/hosts
   127.0.0.1   app.example.com
```

## Quick start (docker-compose)
1. Clone or download this repository
1. Go inside of directory `cd docker-compose/httpd-proxy`
1. Run command:
    - Docker:

          docker network create frontend_network
          docker compose up -d
          (docker compose down)

    - Docker Swarm

          docker network create --driver=overlay frontend_network
          docker stack deploy --compose-file=docker-compose.yml httpd-proxy
