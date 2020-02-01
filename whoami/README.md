# Whoami

## Docker
`docker network create network_backend`
`docker-compose up -d`

## Docker Swarm
`docker network create --driver=overlay network_backend`
`docker stack deploy -c docker-compose.yml whoami`