# Traefik

## Docker
    docker network create frontend_network; \
    docker-compose up -d

## Docker Swarm
    docker network create --driver=overlay frontend_network; \
    docker stack deploy --compose-file=docker-compose.yml traefik

## Let's Encrypt
[Traefik - Let's Encrypt](https://git-scm.com/?target=_blank)
