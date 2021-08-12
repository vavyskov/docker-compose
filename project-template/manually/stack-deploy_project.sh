#!/bin/sh

docker network create --driver=overlay frontend_network
docker network create --driver=overlay project_network

docker stack deploy --compose-file=docker-compose.yml project
docker stack deploy --compose-file=docker-compose.override.yml project
