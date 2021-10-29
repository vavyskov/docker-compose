#!/bin/sh

## Check .env file
if [ ! -f .env ]; then
    printf "\r\n%sFile '.env' does not exist.%s\r\n\r\n" \
    "$(tput setaf 1)" "$(tput sgr 0)"
    exit
else
    ## Get COMPOSE_PROJECT_NAME variable (exists, not comment, not empty)
    if [ -n "$(cat < .env | grep COMPOSE_PROJECT_NAME= | sed '/^#/d' | cut -d= -f2 | xargs)" ]; then
        COMPOSE_PROJECT_NAME=$(cat < .env | grep COMPOSE_PROJECT_NAME= | cut -d= -f2 | xargs)
    else
        printf "\r\n%s'COMPOSE_PROJECT_NAME' variable is not set.%s\r\n\r\n" \
        "$(tput setaf 1)" "$(tput sgr 0)"
        exit
    fi
    ## Get PROJECT_BASE_URL variable (exists, not comment, not empty)
    if [ -n "$(cat < .env | grep PROJECT_BASE_URL= | sed '/^#/d' | cut -d= -f2 | xargs)" ]; then
        PROJECT_BASE_URL=$(cat < .env | grep PROJECT_BASE_URL= | cut -d= -f2 | xargs)
    else
        printf "\r\n%s'PROJECT_BASE_URL' variable is not set.%s\r\n\r\n" \
        "$(tput setaf 1)" "$(tput sgr 0)"
        exit
    fi
    ## Get NGINX_PORT variable (exists, not comment, not empty)
    if [ -n "$(cat < .env | grep NGINX_PORT= | sed '/^#/d' | cut -d= -f2 | xargs)" ]; then
        NGINX_PORT=$(cat < .env | grep NGINX_PORT= | cut -d= -f2 | xargs)
    else
        printf "\r\n%s'NGINX_PORT' variable is not set.%s\r\n\r\n" \
        "$(tput setaf 1)" "$(tput sgr 0)"
        exit
    fi
    ## Get DOCKER_MACHINE_IP variable (exists, not comment, not empty)
    if [ -n "$(cat < .env | grep DOCKER_MACHINE_IP= | sed '/^#/d' | cut -d= -f2 | xargs)" ]; then
        DOCKER_MACHINE_IP=$(cat < .env | grep DOCKER_MACHINE_IP= | cut -d= -f2 | xargs)
    else
        printf "\r\n%s'DOCKER_MACHINE_IP' variable is not set.%s\r\n\r\n" \
        "$(tput setaf 1)" "$(tput sgr 0)"
        exit
    fi
fi

##
## Get variables from .env file
##
#. .env




## Network
docker network create frontend_network
docker network create ${COMPOSE_PROJECT_NAME}_network

## Create and start containers
docker-compose up -d

## TPUT
BLUE_FG=`tput setaf 4`
UNDERLINE=`tput smul`
RESET_ALL=`tput sgr0`

## Show URLs
echo ""
echo "${UNDERLINE}Project URLs:${RESET_ALL}"
echo "${BLUE_FG}http://${DOCKER_MACHINE_IP}:${NGINX_PORT}"
echo "${BLUE_FG}https://${PROJECT_BASE_URL}"
echo "https://adminer-${PROJECT_BASE_URL}"
echo "https://mailcatcher-${PROJECT_BASE_URL}${RESET_ALL}"
echo ""

## Open URLs in browser
## Linux
#xdg-open "http://mailcatcher-${PROJECT_BASE_URL}"
#xdg-open "http://adminer-${PROJECT_BASE_URL}"
#xdg-open "http://${PROJECT_BASE_URL}"
## macOS
#open "http://mailcatcher-${PROJECT_BASE_URL}"
#open "http://adminer-${PROJECT_BASE_URL}"
#open "http://${PROJECT_BASE_URL}"
## Windows
#start "http://mailcatcher-${PROJECT_BASE_URL}" "http://adminer-${PROJECT_BASE_URL}" "http://${PROJECT_BASE_URL}"
