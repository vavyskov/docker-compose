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

## Show URLs
echo ""
tput smul
echo "Project URLs:"
tput rmul
echo "http://${PROJECT_BASE_URL}"
echo "http://adminer.${PROJECT_BASE_URL}"
echo "http://mailcatcher.${PROJECT_BASE_URL}"
echo ""

## Notes
## tput smul # set underline
## tput rmul # remove underline
##
## tput smso # set bold on
## tput rmso # remove bold
##
## tput setaf 1 #red
## tput setaf 2 #green
##
## tput cup 0 0 # move to pos 0,0
##
## tput reset

## Open URLs in browser
## Linux
#xdg-open "http://mailcatcher.${PROJECT_BASE_URL}"
#xdg-open "http://adminer.${PROJECT_BASE_URL}"
#xdg-open "http://${PROJECT_BASE_URL}"
## macOS
#open "http://mailcatcher.${PROJECT_BASE_URL}"
#open "http://adminer.${PROJECT_BASE_URL}"
#open "http://${PROJECT_BASE_URL}"
## Windows
#start "http://mailcatcher.${PROJECT_BASE_URL}" "http://adminer.${PROJECT_BASE_URL}" "http://${PROJECT_BASE_URL}"
