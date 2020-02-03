# Whoami

## Docker
    docker network create frontend; \
    docker-compose up -d`

## Docker Swarm
    docker network create --driver=overlay frontend; \
    docker stack deploy -c docker-compose.yml whoami