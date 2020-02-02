# Whoami

## Docker
    docker network create network_gateway; \
    docker-compose up -d`

## Docker Swarm
    docker network create --driver=overlay network_gateway; \
    docker stack deploy -c docker-compose.yml whoami