# Stack Project

Content:
- Linux
- (E)Nginx
- MySQL/MariaDB
- PostgreSQL
- PHP
- Mailcatcher
- Adminer





## Quick start (docker-compose)

Volitelně Traefik

1. Clone or download this repository
1. Go inside of directory `cd docker-compose/stack-project`
1. Run command:
    - Docker:

          docker network create backend_network; \
          docker network create frontend_network; \
          docker-compose up -d

    - Docker Swarm

          docker network create --driver=overlay backend_network; \
          docker network create --driver=overlay frontend_network; \
          docker stack deploy --compose-file=docker-compose.yml project

## URL

- project.example.com
- project.example.com/adminer | adminer.example.com
- mailcatcher.example.com

## ToDo

- Mailcatcher: project.example.com/mailcatcher
- Swarm Secrets: http://blog.code4hire.com/2018/06/the-rabbit-hole-is-deep-when-trying-to-switch-from-environment-variables-file-to-docker-secrets/
