#!/bin/sh

docker network create --driver=overlay frontend_network
docker network create --driver=overlay lepp_network

docker stack deploy --compose-file=docker-compose.yml lepp
docker stack deploy --compose-file=docker-compose.override.yml lepp
