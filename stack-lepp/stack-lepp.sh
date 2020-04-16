#!/bin/sh

docker network create --driver=overlay frontend_network
docker network create --driver=overlay stack-lepp_network

docker stack deploy --compose-file=docker-compose.yml stack-lepp
docker stack deploy --compose-file=docker-compose.override.yml stack-lepp
