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
    ## Get TRAEFIK_HOSTNAME variable (exists, not comment, not empty)
    if [ -n "$(cat < .env | grep TRAEFIK_HOSTNAME= | sed '/^#/d' | cut -d= -f2 | xargs)" ]; then
        TRAEFIK_HOSTNAME=$(cat < .env | grep TRAEFIK_HOSTNAME= | cut -d= -f2 | xargs)
    else
        printf "\r\n%s'TRAEFIK_HOSTNAME' variable is not set.%s\r\n\r\n" \
        "$(tput setaf 1)" "$(tput sgr 0)"
        exit 1
    fi
    ## Get ADMINER_HOSTNAME variable (exists, not comment, not empty)
    if [ -n "$(cat < .env | grep ADMINER_HOSTNAME= | sed '/^#/d' | cut -d= -f2 | xargs)" ]; then
        ADMINER_HOSTNAME=$(cat < .env | grep ADMINER_HOSTNAME= | cut -d= -f2 | xargs)
    else
        printf "\r\n%s'ADMINER_HOSTNAME' variable is not set.%s\r\n\r\n" \
        "$(tput setaf 1)" "$(tput sgr 0)"
        exit 1
    fi
    ## Get MAILCATCHER_HOSTNAME variable (exists, not comment, not empty)
    if [ -n "$(cat < .env | grep MAILCATCHER_HOSTNAME= | sed '/^#/d' | cut -d= -f2 | xargs)" ]; then
        MAILCATCHER_HOSTNAME=$(cat < .env | grep MAILCATCHER_HOSTNAME= | cut -d= -f2 | xargs)
    else
        printf "\r\n%s'MAILCATCHER_HOSTNAME' variable is not set.%s\r\n\r\n" \
        "$(tput setaf 1)" "$(tput sgr 0)"
        exit 1
    fi
fi

##
## Create networks
##
## $1 ~ network name
## $2 ~ network driver
## https://linuxize.com/post/bash-functions/
create_network() {
    if [ "$(docker network ls | grep "$1" | grep -v "$2")" != "" ]; then
        printf "$(tput setaf 1)Network with name '%s' already exists but requires driver '%s'.$(tput sgr 0)\r\n\r\n" "$1" "$2"
        exit 1
    elif [ "$(docker network ls | grep "$1" | grep "$2")" = "" ]; then
        printf "Creating network '%s'...\r\n" "$1"
        docker network create --driver "$2" "$1"
    else
        printf "Network with name '%s' already exists.\r\n" "$1"
    fi
}
## Empty new line
printf "\r\n"
## https://linuxize.com/post/bash-for-loop/
for i in frontend_network backend_network database_network
do
  create_network "$i" bridge
done

## Create and start containers
docker-compose --env-file .env up -d

## TPUT
BLUE_FG=`tput setaf 4`
UNDERLINE=`tput smul`
RESET_ALL=`tput sgr0`

## Show URLs
echo ""
echo "${UNDERLINE}Project URLs:${RESET_ALL}"
echo "${BLUE_FG}https://${TRAEFIK_HOSTNAME}${RESET_ALL}"
echo "${BLUE_FG}https://${ADMINER_HOSTNAME}${RESET_ALL}"
echo "${BLUE_FG}https://${MAILCATCHER_HOSTNAME}${RESET_ALL}"
echo ""
