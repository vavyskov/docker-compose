#!/bin/sh

## Stop and remove resources
docker-compose down

## Remove all unused networks
docker network prune -f
