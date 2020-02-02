# Traefik

## Docker
`docker network create network_gateway`
`docker-compose up -d`

## Docker Swarm
`docker network create --driver=overlay network_gateway`
`docker stack deploy -c docker-compose.yml traefik`

## Let's Encrypt
[Traefik - Let's Encrypt](https://git-scm.com/?target=_blank)
