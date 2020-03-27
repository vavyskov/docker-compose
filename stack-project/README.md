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
