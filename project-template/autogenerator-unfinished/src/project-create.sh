#!/bin/sh
set -e

##
## Update Docker images and create Docker project
##

## Check Docker Daemon
if [ "$(docker container ls 1>/dev/null 2>/dev/null; echo $?)" != 0 ]; then
    printf "\r\n%sCannot connect to the 'Docker Daemon'. Is the Docker Daemon running?%s\r\n\r\n" \
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
    if [ -n "$(cat < .env | grep COMPOSE_PROJECT_NAME= | sed '/^#/d' | cut -d= -f2 | xargs)" ]; then
        COMPOSE_PROJECT_NAME=$(cat < .env | grep COMPOSE_PROJECT_NAME= | cut -d= -f2 | xargs)
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
        *)
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
            *)
                echo "Answer '$(tput setaf 2)yes$(tput sgr 0)' or '$(tput setaf 2)no$(tput sgr 0)'."
            ;;
        esac
    done
fi

##
## Create project
##

## .sh variables
NETWORK_FRONTEND=frontend_network
NETWORK_PROJECT="${COMPOSE_PROJECT_NAME}_network"

## Update images
if [ $UPDATE = true ]; then
    printf "\r\nPulling images...\r\n"
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
printf "\r\nCreating network...\r\n"
for i in $NETWORK_FRONTEND $NETWORK_PROJECT
do
  create_network "$i" $NETWORK_DRIVER
done

##
## Convert .secrets.env file to secrets and environment variables
##
#printf "\r\nConverting '.secrets.env' file...\r\n"
#while read -r line; do
#    ## Eliminate any lines that are empty, or start with # (comments)
#    if [ -z "$line" ] || [ "$line" != "$(echo "$line" | sed '/^#/d')" ]; then
#        continue
#    fi
#
#    ## Split the line by '=' and change name to lower characters
#    SECRET_NAME=$(echo "$line" | cut -d= -f1 | tr '[:upper:]' '[:lower:]')
#    SECRET_VALUE=$(echo "$line" | cut -d= -f2 | xargs)
#
#    if [ $SWARM_MODE = true ]; then
#        ## Remove old secret
#        if [ "$(docker secret ls | grep "$SECRET_NAME")" != "" ]; then
#            docker secret rm "${COMPOSE_PROJECT_NAME}_${SECRET_NAME}" >/dev/null
#        fi
#
#        ## Create new secret
#        echo "${SECRET_VALUE}" | docker secret create "${COMPOSE_PROJECT_NAME}_${SECRET_NAME}" - >/dev/null
#        ## Create new secret (remove line break and trim whitespace)
#        ## Example: echo 'rn=rn \r \n ' | hexdump -C
#        ## Example: echo 'rn=rn \r \n ' | sed 's/\\r//g' | sed 's/\\n//g' | xargs | hexdump -C
#        #echo "$SECRET_VALUE" | sed 's/\\r//g' | sed 's/\\n//g' | xargs | docker secret create "${COMPOSE_PROJECT_NAME}_${SECRET_NAME}" - >/dev/null
#
#        ## Declare environment
#        eval "$(echo "${SECRET_NAME}" | tr '[:lower:]' '[:upper:]')=/run/secrets/${COMPOSE_PROJECT_NAME}_${SECRET_NAME}"
#    else
#        ## Declare environment
#        eval "$(echo "${SECRET_NAME}" | tr '[:lower:]' '[:upper:]')='${SECRET_VALUE}'"
#    fi
#done < .secrets.env

##
## Get variables from .env file
##
. .env




## ENV substitution not working :(
#envsubst  < docker-compose.override.yml-backup > test.yml



##
## Create docker-compose.yml file
##
cat << EOF > docker-compose.yml
version: '3.5'

services:
  php-fpm:
    image: vavyskov/php:${PHP_VERSION}
    container_name: ${COMPOSE_PROJECT_NAME}_php-fpm
    #hostname: "web_app_fpm"
    ## Docker Swarm (docker stack deploy) does not support "depends_on" :(
    #depends_on:
    #  - mariadb
    #  - postgres
    environment:
      #FASTCGI_PORT: ${FASTCGI_PORT}
      PROJECT_MODE: ${PROJECT_MODE}
      #PHP_HOME: ${PHP_HOME}
      PHP_USER: ${PHP_USER}
      SMTP_HOSTNAME: ${SMTP_HOSTNAME}
      SMTP_PORT: ${SMTP_PORT}
      SMTP_FROM: ${SMTP_FROM}
      SMTP_USER: ${SMTP_USER}
      SMTP_PASSWORD: ${SMTP_PASSWORD}
#      PROXY_SERVER: ${PROXY_SERVER}
      XDEBUG_HOSTNAME: ${XDEBUG_HOSTNAME}
      #APP_ENV: ${APP_ENV}
      #APP_SECRET: ${APP_SECRET}
      #DATABASE_HOSTNAME: mysql://${MARIADB_USER}:${MARIADB_PASSWORD}@database:3306/${MARIADB_DATABASE}?serverVersion=5.7
    networks:
      - project_network
    volumes:
      - html_data:${PROJECT_ROOT}
      #- ~/.ssh:${SSH_HOME}/.shared/.ssh:ro
      #- ~/.gitconfig:${SSH_HOME}/.shared/.gitconfig:ro
    #working_dir: /var/www/html
    deploy:
      replicas: 1

networks:
  project_network:
    external: true

volumes:
  html_data:
    name: ${COMPOSE_PROJECT_NAME}_html_data
#    driver_opts:
#      type: nfs
#      o: addr=${NFS_HOSTNAME},nolock,soft,rw
#      device: :${NFS_PATH}/${COMPOSE_PROJECT_NAME}/volumes/html_data

EOF

##
## Create docker-compose.override.yml file
##
cat << EOF > docker-compose.override.yml
version: '3.5'

#configs:
#  nginx_config:
#    name: nginx-config-${NGINX_CONFIG:-1}
#    file: ./config/nginx.conf

services:
  nginx:
    image: vavyskov/nginx:${NGINX_VERSION}
    container_name: ${COMPOSE_PROJECT_NAME}_nginx
    hostname: ${PROJECT_HOSTNAME}
    #hostname: project_nginx (docker service name)
    volumes:
      ## 'nocopy' flag to disable copying of data from a container when a volume is created
      - html_data:${PROJECT_ROOT}:nocopy
#      - /etc/ss/path:/etc/ssl/path:ro
      #- ./logs/nginx:/var/log/nginx
      #- /etc/localtime:/etc/localtime:ro
      #- /etc/timezone:/etc/timezone:ro
    ## Docker Swarm (docker stack deploy) does not support "depends_on" :(
    depends_on:
      - php-fpm
    #environment:
      #ACCESS_LOG: ${ACCESS_LOG}
      #ERROR_LOG: ${ERROR_LOG}
      #NGINX_ROOT: ${NGINX_ROOT}
      #FASTCGI_HOSTNAME: ${FASTCGI_HOSTNAME}
      #FASTCGI_PORT: ${FASTCGI_PORT}
#      CERTIFICATE_PATH: ${CERTIFICATE_PATH}
#      CERTIFICATE_FILENAME: ${CERTIFICATE_FILENAME}
#      CERTIFICATE_KEYNAME: ${CERTIFICATE_KEYNAME}
    ## Docker Config - store non-sensitive data as configuration files (not encrypted)
    ## cat nginx.conf | docker config create project_nginx.conf -
    #configs:
    #  - source: nginx_config
    #    target: /etc/nginx/nginx.conf
    #ports:
    #  - target: 80
    #    published: ${NGINX_PORT}
    #    #mode: host
    #  - target: 443
    #    published: ${NGINX_PORT_SSL}
    #    #mode: host
    networks:
      - frontend_network
      #frontend_network:
      #  aliases:
      #    - ${PROJECT_HOSTNAME}
      - project_network
    deploy:
      replicas: 1
      placement:
        constraints:
          - node.role == manager
          #- node.role == worker
          #- node.hostname == serverhostname
    #logging:
    #  driver: json-file
    #  options:
    #    max-size: 10m
    #    max-file: 3
    labels:
      - traefik.enable=true
      - traefik.http.services.${COMPOSE_PROJECT_NAME}_nginx.loadbalancer.server.port=80
      - traefik.http.routers.${COMPOSE_PROJECT_NAME}_nginx.rule=Host(\`${PROJECT_HOSTNAME}\`)
#     - traefik.http.routers.${COMPOSE_PROJECT_NAME}_nginx.tls=true
      #- traefik.http.routers.${COMPOSE_PROJECT_NAME}_nginx.service=${COMPOSE_PROJECT_NAME}_nginx
      #- traefik.http.routers.${COMPOSE_PROJECT_NAME}_nginx.entrypoints=websecure
      #- traefik.http.services.${COMPOSE_PROJECT_NAME}_nginx.loadbalancer.passhostheader=true
    #healthcheck:
    #  test: curl --fail -s http://localhost:5000/ || exit 1
    #  ##test: "/usr/bin/curl --silent --fail -o /dev/null -w %{http_code} http://localhost:9200 || exit 1"
    #  ##test: "/bin/nc -z -w3 localhost 5000 || exit 1"
    #  ##interval: 1m30s
    #  interval: 30s
    #  timeout: 10s
    #  retries: 3

  ssh:
    image: vavyskov/ssh:${SSH_VERSION}
    container_name: ${COMPOSE_PROJECT_NAME}_ssh
#    hostname: ${PROJECT_HOSTNAME}
    #hostname: project_ssh (docker service name)
    ## Docker Swarm (docker stack deploy) does not support "depends_on" :(
    depends_on:
      - php-fpm
#    secrets:
#      - project_ssh_password
    environment:
      PROJECT_MODE: ${PROJECT_MODE}
      SSH_HOME: ${SSH_HOME}
      SSH_USER: ${SSH_USER}
      SSH_PASSWORD: ${SSH_PASSWORD}
      GIT_EMAIL: ${GIT_EMAIL}
      GIT_NAME: ${GIT_NAME}
      SMTP_HOSTNAME: ${SMTP_HOSTNAME}
      SMTP_PORT: ${SMTP_PORT}
      SMTP_FROM: ${SMTP_FROM}
      ## SMTP user example: ${SMTP_USER}
      SMTP_USER: ${SMTP_USER}
      SMTP_PASSWORD: ${SMTP_PASSWORD}
      PROXY_SERVER: ${PROXY_SERVER}
      XDEBUG_HOSTNAME: ${XDEBUG_HOSTNAME}
      #APP_ENV: ${APP_ENV}
      #APP_SECRET: ${APP_SECRET}
      #DATABASE_HOSTNAME: mysql://${MARIADB_USER}:${MARIADB_PASSWORD}@database:3306/${MARIADB_DATABASE}?serverVersion=5.7
    ports:
      ## https://community.containo.us/t/routing-ssh-traffic-with-traefik-v2/717/13
      - target: 22
        published: ${SSH_PORT}
      #- target: 9000
      #  published: ${XDEBUG_PORT}
    networks:
      - project_network
    volumes:
      ## 'nocopy' flag to disable copying of data from a container when a volume is created
      - html_data:${PROJECT_ROOT}:nocopy
#      - ~/.ssh:${SSH_HOME}/.shared/.ssh:ro
#      - ~/.gitconfig:${SSH_HOME}/.shared/.gitconfig:ro
    #working_dir: /var/www/html
    deploy:
      #mode: replicated
      replicas: 1

  mariadb:
    image: mariadb:${MARIADB_VERSION}
    container_name: ${COMPOSE_PROJECT_NAME}_mariadb
    environment:
      MYSQL_DATABASE: ${MARIADB_DATABASE}
      MYSQL_USER: ${MARIADB_USER}
      MYSQL_PASSWORD: ${MARIADB_PASSWORD}
      MYSQL_ROOT_PASSWORD: ${MARIADB_ROOT_PASSWORD}
    command: ["mysqld", "--character-set-server=utf8mb4", "--collation-server=utf8mb4_czech_ci"]
    volumes:
      #- ./mariadb/init.sql:/docker-entrypoint-initdb.d/init.sql
      - mariadb_data:/var/lib/mysql
    ports:
      - target: 3306
        published: ${MARIADB_PORT}
    networks:
      - project_network
    #restart: unless-stopped
    #restart: always
    deploy:
      replicas: 1
      #update_config:
      #  failure_action: rollback
      #  parallelism: 1
      #  delay: 5s
      #restart_policy:
      #  condition: on-failure
      #  delay: 5s
      #  max_attempts: 3
      #resources:
      #  limits:
      #    cpus: '0.1'
      #    memory: 2G
      #  reservations:
      #    cpus: '0.0001'
      #    memory: 50M

  postgres:
    image: postgres:${POSTGRES_VERSION}
    container_name: ${COMPOSE_PROJECT_NAME}_postgres
    secrets:
      - postgres_password
    environment:
      POSTGRES_USER: ${POSTGRES_USER}
#      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
      POSTGRES_PASSWORD_FILE: /run/secrets/postgres_password
      POSTGRES_DB: ${POSTGRES_DATABASE}
      LC_COLLATE: utf8mb4_czech_ci
      LC_CTYPE: utf8mb4_czech_ci
      #PGDATA: /data/postgres
    volumes:
      - postgres_data:/var/lib/postgresql/data
       #- postgres:/data/postgres
    ports:
      - target: 5432
        published: ${POSTGRES_PORT}
    networks:
      - project_network
    #restart: unless-stopped
    #restart: always
    deploy:
      replicas: 1
      #update_config:
      #  failure_action: rollback
      #  parallelism: 1
      #  delay: 5s
      #restart_policy:
      #  condition: on-failure
      #  delay: 5s
      #  max_attempts: 3
      #resources:
      #  limits:
      #    cpus: '0.1'
      #    memory: 2G
      #  reservations:
      #    cpus: '0.0001'
      #    memory: 50M

  mailcatcher:
    image: vavyskov/mailcatcher:${MAILCATCHER_VERSION}
    container_name: ${COMPOSE_PROJECT_NAME}_mailcatcher
    #hostname: project_mailcatcher (docker service name)
    #hostname: ${MAILCATCHER_HOSTNAME}
    #hostname: ${MAILCATCHER_HOSTNAME} # /mailcatcher
    ports:
      - target: 80
        published: ${MAILCATCHER_PORT}
      - target: 25
        published: ${SMTP_PORT}
    networks:
      - frontend_network
    deploy:
      replicas: 1
      placement:
        constraints:
          - node.role == manager
    labels:
      - traefik.enable=true
      - traefik.http.services.${COMPOSE_PROJECT_NAME}_mailcatcher.loadbalancer.server.port=80
      - traefik.http.routers.${COMPOSE_PROJECT_NAME}_mailcatcher.rule=Host(\`${MAILCATCHER_HOSTNAME}\`)
      #- traefik.http.routers.${COMPOSE_PROJECT_NAME}_mailcatcher.rule=Host(\`${PROJECT_HOSTNAME}\`) && Path(\`${MAILCATCHER_PATH}\`)
#      - traefik.http.routers.${COMPOSE_PROJECT_NAME}_mailcatcher.tls=true
      #- traefik.http.routers.${COMPOSE_PROJECT_NAME}_mailcatcher.entrypoints=websecure
      #- traefik.http.routers.${COMPOSE_PROJECT_NAME}_mailcatcher.service=mailcatcher

  adminer:
    image: adminer:${ADMINER_VERSION}
    container_name: ${COMPOSE_PROJECT_NAME}_adminer
    #hostname: project_adminer (docker service name)
    #hostname: ${MAILCATCHER_HOSTNAME}
    #hostname: ${MAILCATCHER_HOSTNAME} # /mailcatcher
    ports:
      - target: 8080
        published: ${ADMINER_PORT}
    networks:
      - frontend_network
      - project_network
    deploy:
      replicas: 1
      placement:
        constraints:
          - node.role == manager
    labels:
      - traefik.enable=true
      - traefik.http.services.${COMPOSE_PROJECT_NAME}_adminer.loadbalancer.server.port=8080
      #- traefik.http.routers.${COMPOSE_PROJECT_NAME}_adminer.rule=Host(\`${ADMINER_HOSTNAME}\`)
      - traefik.http.routers.${COMPOSE_PROJECT_NAME}_adminer.rule=Host(\`${PROJECT_HOSTNAME}\`) && Path(\`${ADMINER_PATH}\`)
#      - traefik.http.routers.${COMPOSE_PROJECT_NAME}_adminer.tls=true
      #- traefik.http.routers.${COMPOSE_PROJECT_NAME}_adminer.entrypoints=websecure
      #- traefik.http.routers.${COMPOSE_PROJECT_NAME}_adminer.service=adminer

networks:
  frontend_network:
    external: true
  project_network:
    external: true

volumes:
  html_data:
    name: ${COMPOSE_PROJECT_NAME}_html_data
#    driver_opts:
#      type: nfs
#      o: addr=${NFS_HOSTNAME},nolock,soft,rw
#      device: :${NFS_PATH}/${COMPOSE_PROJECT_NAME}/volumes/html_data
  mariadb_data:
    name: ${COMPOSE_PROJECT_NAME}_mariadb_data
#    driver_opts:
#      type: nfs
#      o: addr=${NFS_HOSTNAME},nolock,soft,rw
#      device: :${NFS_PATH}/${COMPOSE_PROJECT_NAME}/volumes/mariadb_data
  postgres_data:
    name: ${COMPOSE_PROJECT_NAME}_postgres_data
#    driver_opts:
#      type: nfs
#      o: addr=${NFS_HOSTNAME},nolock,soft,rw
#      device: :${NFS_PATH}/${COMPOSE_PROJECT_NAME}/volumes/postgres_data

secrets:
#  project_ssh_password:
#    external: true
  postgres_password:
    file: ./secrets/POSTGRES_PASSWORD

EOF

##
## Create project
##
printf "\r\nCreating project...\r\n"
if [ $SWARM_MODE != true ]; then
    ## Show only Error not Warning
    docker-compose --log-level ERROR up -d
else
    # ToDo: Show only Error not Warning ("--log-level" | 2>&1 | 2>/dev/null)
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