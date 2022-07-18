#!/bin/sh

## Check .env file
if [ ! -f .env ]; then
    printf "\r\n%sFile '.env' does not exist.%s\r\n\r\n" \
    "$(tput setaf 1)" "$(tput sgr 0)"
    exit 1
else
    ## Get COMPOSE_PROJECT_NAME variable (exists, not comment, not empty)
    if [ -n "$(cat < .env | grep COMPOSE_PROJECT_NAME= | sed '/^#/d' | cut -d= -f2 | xargs)" ]; then
        COMPOSE_PROJECT_NAME=$(cat < .env | grep COMPOSE_PROJECT_NAME= | cut -d= -f2 | xargs)
    else
        printf "\r\n%s'COMPOSE_PROJECT_NAME' variable is not set.%s\r\n\r\n" \
        "$(tput setaf 1)" "$(tput sgr 0)"
        exit 1
    fi
fi

## Network
docker network create --driver=overlay frontend_network
docker network create --driver=overlay ${COMPOSE_PROJECT_NAME}_network

## Part 1
## docker stack deploy --compose-file=docker-compose.yml project
docker-compose --file=docker-compose.yml config | docker stack deploy --compose-file - ${COMPOSE_PROJECT_NAME}

## Part 2 (depends on "Part 1")
## (docker stack deploy --compose-file=docker-compose.override.yml project)
## docker-compose config | docker stack deploy --compose-file - project
## Require remove "depends_on" section (https://unix.stackexchange.com/questions/648684/how-do-i-remove-all-specifc-sub-sections-of-a-specifc-header-in-a-yaml-file?rq=1#answer-650052)
docker-compose config | sed -e 'H;x;/^\(  *\)\n\1/{s/\n.*//;x;d;}' -e 's/.*//;x;/\depends_on/{s/^\( *\).*/ \1/;x;d;}' | docker stack deploy --compose-file - ${COMPOSE_PROJECT_NAME}