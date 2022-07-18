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
    ## Get PROJECT_BASE_URL variable (exists, not comment, not empty)
    if [ -n "$(cat < .env | grep PROJECT_BASE_URL= | sed '/^#/d' | cut -d= -f2 | xargs)" ]; then
        PROJECT_BASE_URL=$(cat < .env | grep PROJECT_BASE_URL= | cut -d= -f2 | xargs)
    else
        printf "\r\n%s'PROJECT_BASE_URL' variable is not set.%s\r\n\r\n" \
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
for i in frontend_network ${COMPOSE_PROJECT_NAME}_network
do
  create_network "$i" bridge
done

## Create and start containers
docker-compose up -d

## TPUT
BLACK_FG=`tput setaf 0`
RED_FG=`tput setaf 1`
GREEN_FG=`tput setaf 2`
YELLOW_FG=`tput setaf 3`
BLUE_FG=`tput setaf 4`
MAGENTA_FG=`tput setaf 5`
CYAN_FG=`tput setaf 6`
WHITE_FG=`tput setaf 7`
RESET_FG=`tput setaf 9`

BLACK_BG=`tput setab 0`
RED_BG=`tput setab 1`
GREEN_BG=`tput setab 2`
YELLOW_BG=`tput setab 3`
BLUE_BG=`tput setab 4`
MAGENTA_BG=`tput setab 5`
CYAN_BG=`tput setab 6`
WHITE_BG=`tput setab 7`
RESET_BG=`tput setab 9`

MOVE_UP=`tput cuu 1`
MOVE_TO_0_0=`tput cup 0 0`
CLEAR_LINE=`tput el 1`

UNDERLINE=`tput smul`
RESET_UNDERLINE=`tput rmul`
INVERSE=`tput smso` # Start "standout" mode (tput rev)
RESET_INVERSE=`tput rmso` # End "standout" mode

BOLD=`tput bold`
BLINK=`tput blink`
INVISIBLE=`tput invis`

CLAER_TERMINAL=`tput reset` ## (tput init | reset)
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
