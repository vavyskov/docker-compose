#!/bin/sh
set -e

##
## Update Docker images and create Docker project
##

## Check Docker daemon
if [ "$(docker ps 1>/dev/null 2>/dev/null; echo $?)" != 0 ]; then
    printf "\r\n%sCannot connect to the Docker daemon. Is the docker daemon running?%s\r\n\r\n" \
    "$(tput setaf 1)" "$(tput sgr 0)"

    exit
fi

## Check .env file
if [ ! -f .env ]; then
    printf "\r\n%sFile '.env' does not exist.%s\r\n\r\n" \
    "$(tput setaf 1)" "$(tput sgr 0)"
    exit
else
    ## Get COMPOSE_PROJECT_NAME variable (exists, not comment, not empty)
    if [ -n "$(cat < .env | grep COMPOSE_PROJECT_NAME= | sed '/^#/d' | cut -d= -f2)" ]; then
        COMPOSE_PROJECT_NAME=$(cat < .env | grep COMPOSE_PROJECT_NAME= | cut -d= -f2)
    else
        printf "\r\n%s'COMPOSE_PROJECT_NAME' variable is not set.%s\r\n\r\n" \
        "$(tput setaf 1)" "$(tput sgr 0)"
        exit
    fi
fi

##
## Get variables from UI
##

## Update Docker images?
printf "\r\n%sDo you want to update stack images? (yes/no)%s [%syes%s]:\r\n" \
"$(tput setaf 2)" "$(tput sgr 0)" "$(tput setaf 3)" "$(tput sgr 0)"
while
    tput bel
    printf "> "
    read -r UPDATE
do
    case $UPDATE in
        [Yy]*|'')
            if [ "$UPDATE" = '' ]; then
                tput cuu 1
                tput cuf 2
                echo 'yes'
            fi
            UPDATE=true
            break
        ;;
        [Nn]*)
            UPDATE=false
            break
        ;;
        * )
            echo "Answer '$(tput setaf 2)yes$(tput sgr 0)' or '$(tput setaf 2)no$(tput sgr 0)'."
        ;;
    esac
done

## Docker Swarm mode with active leader?
if [ "$(docker node ls 1>/dev/null 2>/dev/null; echo $?)" = 0 ] \
&& [ "$(docker node ls 2>/dev/null | grep Leader | grep Active)" != "" ]; then
    printf "\r\n%sDo you want to use Docker Swarm mode? (yes/no)%s [%syes%s]:\r\n" \
    "$(tput setaf 2)" "$(tput sgr 0)" "$(tput setaf 3)" "$(tput sgr 0)"

    while
        tput bel
        printf "> "
        read -r SWARM_MODE
    do
        case $SWARM_MODE in
            [Yy]*|'')
                if [ "$SWARM_MODE" = '' ]; then
                    tput cuu 1
                    tput cuf 2
                    echo 'yes'
                fi
                SWARM_MODE=true
                break
            ;;
            [Nn]*)
                break
            ;;
            * )
                echo "Answer '$(tput setaf 2)yes$(tput sgr 0)' or '$(tput setaf 2)no$(tput sgr 0)'."
            ;;
        esac
    done
fi

## Convert .env file to secrets
printf "\r\nConverting '.env' file to secrets...\r\n"
if [ $SWARM_MODE = true ]; then
    while read -r line; do
        ## Eliminate any lines that are empty, or start with # (comments)
        if [ -z "$line" ] || [ "$line" != "$(echo "$line" | sed '/^#/d')" ]; then
            continue
        fi

        ## Split the line by '=' and change name to lower characters
        SECRET_NAME=$(echo "$line" | cut -d= -f1 | tr '[:upper:]' '[:lower:]')
        SECRET_VALUE=$(echo "$line" | cut -d= -f2)

        ## Remove old secret
        if [ "$(docker secret ls | grep "$SECRET_NAME")" != "" ]; then
            docker secret rm "${COMPOSE_PROJECT_NAME}_${SECRET_NAME}" >/dev/null
        fi

        ## Create new secret
        echo "$SECRET_VALUE" | docker secret create "${COMPOSE_PROJECT_NAME}_${SECRET_NAME}" - >/dev/null
        ## Create new secret (remove line break and trim whitespace)
        ## Example: echo 'rn=rn \r \n ' | hexdump -C
        ## Example: echo 'rn=rn \r \n ' | sed 's/\\r//g' | sed 's/\\n//g' | xargs | hexdump -C
        #echo "$SECRET_VALUE" | sed 's/\\r//g' | sed 's/\\n//g' | xargs | docker secret create "${COMPOSE_PROJECT_NAME}_${SECRET_NAME}" - >/dev/null
    done < .env
fi

##
## Create project
##

## .sh variables
NETWORK_FRONTEND=frontend_network
NETWORK_PROJECT="${COMPOSE_PROJECT_NAME}_network"

## New line
printf "\r\n"

## Update images
if [ $UPDATE = true ]; then
    printf "Pulling images...\r\n"
    docker-compose pull 2>/dev/null
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
        exit
    elif [ "$(docker network ls | grep "$1" | grep "$2")" = "" ]; then
        docker network create --driver "$2" "$1"
    fi
}

## Set network driver
if [ $SWARM_MODE != true ]; then
    NETWORK_DRIVER=bridge
else
    NETWORK_DRIVER=overlay
fi

## https://linuxize.com/post/bash-for-loop/
for i in $NETWORK_FRONTEND $NETWORK_PROJECT
do
  create_network "$i" $NETWORK_DRIVER
done

##
## Create project
##
if [ $SWARM_MODE != true ]; then
    docker-compose up -d
else
    docker stack deploy --compose-file=docker-compose.yml "$COMPOSE_PROJECT_NAME"
    docker stack deploy --compose-file=docker-compose.override.yml "$COMPOSE_PROJECT_NAME"
fi

#printf "$(tput setaf 2)Swarm mode$(tput sgr 0): %s\r\n\r\n" $SWARM_MODE




##
## tput
##
## Foreground & background colour commands:
## tput setab [1-7] # Set the background colour using ANSI escape
## tput setaf [1-7] # Set the foreground colour using ANSI escape
##
## Num  Colour    #define         R G B
## 0    black     COLOR_BLACK     0,0,0
## 1    red       COLOR_RED       1,0,0
## 2    green     COLOR_GREEN     0,1,0
## 3    yellow    COLOR_YELLOW    1,1,0
## 4    blue      COLOR_BLUE      0,0,1
## 5    magenta   COLOR_MAGENTA   1,0,1
## 6    cyan      COLOR_CYAN      0,1,1
## 7    white     COLOR_WHITE     1,1,1
##
## Text mode commands:
## tput bold    # Select bold mode
## tput dim     # Select dim (half-bright) mode
## tput smul    # Enable underline mode
## tput rmul    # Disable underline mode
## tput rev     # Turn on reverse video mode
## tput smso    # Enter standout (bold) mode
## tput rmso    # Exit standout mode
##
## Cursor movement commands:
## tput cup Y X # Move cursor to screen postion X,Y (top left is 0,0)
## tput cuf N   # Move N characters forward (right)
## tput cub N   # Move N characters back (left)
## tput cuu N   # Move N lines up
## tput ll      # Move to last line, first column (if no cup)
## tput sc      # Save the cursor position
## tput rc      # Restore the cursor position
## tput lines   # Output the number of lines of the terminal
## tput cols    # Output the number of columns of the terminal
##
## Clear and insert commands:
## tput ech N   # Erase N characters
## tput clear   # Clear screen and move the cursor to 0,0
## tput el 1    # Clear to beginning of line
## tput el      # Clear to end of line
## tput ed      # Clear to end of screen
## tput ich N   # Insert N characters (moves rest of line forward!)
## tput il N    # Insert N lines
##
## Other commands
## tput sgr0    # Reset text format to the terminal's default
## tput bel     # Play a bell
##
## Scripts:
## echo -e "setf 7\r\nsetb 1" | tput -S  # set fg white and bg red