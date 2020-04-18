#!/bin/sh
set -e

## Docker create (build, compose) script

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
## echo -e "setf 7\nsetb 1" | tput -S  # set fg white and bg red

SWARM_MODE=false
NETWORK_FRONTEND=frontend_network
NETWORK_PROJECT=project_network

## Docker
if [ "$(docker ps 1>/dev/null 2>/dev/null; echo $?)" != 0 ]; then
    printf "\r\nCannot connect to the Docker daemon. Is the docker daemon running?\r\n\r\n"
    exit
fi

## Docker Swarm mode with active leader
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
                SWARM_MODE=true
                break
            ;;
            [Nn]*)
                SWARM_MODE=false
                break
            ;;
            * )
                echo "Answer '$(tput setaf 2)yes$(tput sgr 0)' or '$(tput setaf 2)no$(tput sgr 0)'."
            ;;
        esac
    done
fi

## Update images
docker-compose pull

## Set network driver
if [ ${SWARM_MODE} = false ]; then
    NETWORK_DRIVER=bridge
else
    NETWORK_DRIVER=overlay
fi

## Create frontend network
if [ "$(docker network ls | grep ${NETWORK_FRONTEND})" = "" ]; then
    docker network create --driver ${NETWORK_DRIVER} ${NETWORK_FRONTEND}
fi

## Create project network
if [ "$(docker network ls | grep ${NETWORK_PROJECT})" = "" ]; then
    docker network create --driver ${NETWORK_DRIVER} ${NETWORK_FRONTEND}
fi

## Create project
if [ ${SWARM_MODE} = false ]; then
    docker-compose up -d
else
    docker stack deploy --compose-file=docker-compose.yml project
    docker stack deploy --compose-file=docker-compose.override.yml project
fi

#printf "$(tput setaf 2)Swarm mode$(tput sgr 0): %s\r\n\r\n" ${SWARM_MODE}
