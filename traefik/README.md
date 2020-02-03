# Traefik

## Docker
    docker network create frontend; \
    docker-compose up -d

## Docker Swarm
    docker network create --driver=overlay frontend; \
    docker stack deploy -c docker-compose.yml traefik

## Let's Encrypt
[Traefik - Let's Encrypt](https://git-scm.com/?target=_blank)
