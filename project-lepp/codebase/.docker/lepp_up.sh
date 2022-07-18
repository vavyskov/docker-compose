#!/bin/sh

## Check .env file
if [ ! -f .env ]; then
    printf "\r\n%sFile '.env' does not exist.%s\r\n\r\n" \
    "$(tput setaf 1)" "$(tput sgr 0)"
    exit 1
else



    ## ToDo: Get variables from .env file
    ## "." and "source" works in macOS
    #. .env
    #source .env



    ## Get COMPOSE_PROJECT_NAME variable (exists, not comment, not empty)
    if [ -n "$(cat < .env | grep COMPOSE_PROJECT_NAME= | sed '/^#/d' | cut -d= -f2 | xargs)" ]; then
        COMPOSE_PROJECT_NAME=$(cat < .env | grep COMPOSE_PROJECT_NAME= | cut -d= -f2 | xargs)
    else
        printf "\r\n%s'COMPOSE_PROJECT_NAME' variable is not set.%s\r\n\r\n" \
        "$(tput setaf 1)" "$(tput sgr 0)"
        exit 1
    fi
    ## Get PROJECT_HOSTNAME variable (exists, not comment, not empty)
    if [ -n "$(cat < .env | grep PROJECT_HOSTNAME= | sed '/^#/d' | cut -d= -f2 | xargs)" ]; then
        PROJECT_HOSTNAME=$(cat < .env | grep PROJECT_HOSTNAME= | cut -d= -f2 | xargs)
    else
        printf "\r\n%s'PROJECT_HOSTNAME' variable is not set.%s\r\n\r\n" \
        "$(tput setaf 1)" "$(tput sgr 0)"
        exit 1
    fi
    ## Get NGINX_PORT variable (exists, not comment, not empty)
    if [ -n "$(cat < .env | grep NGINX_PORT= | sed '/^#/d' | cut -d= -f2 | xargs)" ]; then
        NGINX_PORT=$(cat < .env | grep NGINX_PORT= | cut -d= -f2 | xargs)
    else
        printf "\r\n%s'NGINX_PORT' variable is not set.%s\r\n\r\n" \
        "$(tput setaf 1)" "$(tput sgr 0)"
        exit 1
    fi
    ## Get DOCKER_MACHINE_IP variable (exists, not comment, not empty)
    if [ -n "$(cat < .env | grep DOCKER_MACHINE_IP= | sed '/^#/d' | cut -d= -f2 | xargs)" ]; then
        DOCKER_MACHINE_IP=$(cat < .env | grep DOCKER_MACHINE_IP= | cut -d= -f2 | xargs)
    else
        printf "\r\n%s'DOCKER_MACHINE_IP' variable is not set.%s\r\n\r\n" \
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
for i in frontend_network mailcatcher_network adminer_network ${COMPOSE_PROJECT_NAME}_network
do
  create_network "$i" bridge
done

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
echo "${BLUE_FG}https://${PROJECT_HOSTNAME}"
echo "https://adminer-${PROJECT_HOSTNAME}"
echo "https://mailcatcher-${PROJECT_HOSTNAME}${RESET_ALL}"
echo ""

## Open URLs in browser
## Linux
#xdg-open "http://mailcatcher-${PROJECT_HOSTNAME}"
#xdg-open "http://adminer-${PROJECT_HOSTNAME}"
#xdg-open "http://${PROJECT_HOSTNAME}"
## macOS
#open "http://mailcatcher-${PROJECT_HOSTNAME}"
#open "http://adminer-${PROJECT_HOSTNAME}"
#open "http://${PROJECT_HOSTNAME}"
## Windows
#start "http://mailcatcher-${PROJECT_HOSTNAME}" "http://adminer-${PROJECT_HOSTNAME}" "http://${PROJECT_HOSTNAME}"
