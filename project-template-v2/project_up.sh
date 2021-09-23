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
fi

## Network
docker network create frontend_network
docker network create ${COMPOSE_PROJECT_NAME}_network

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
