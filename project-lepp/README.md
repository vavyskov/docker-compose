# Project LEPP

Content:
- Linux
- (E)Nginx
- PostgreSQL
- PHP

## Quick start (docker-compose)

1. Clone or download this repository.
1. Go inside of directory `cd docker-compose/project-lepp/docker`.
1. Run command:
    - Docker:

          docker network create frontend_network
          docker network create mailcatcher_network
          docker network create adminer_network
          docker network create lepp_network
          docker-compose up -d

    - Docker Swarm
          
          docker network create --driver=overlay frontend_network
          docker network create --driver=overlay mailcatcher_network
          docker network create --driver=overlay adminer_network
          docker network create --driver=overlay lepp_network          
          docker stack deploy --compose-file=docker-compose.yml lepp
          docker stack deploy --compose-file=docker-compose.override.yml lepp

## Notes

Docker Swarm (docker stack deploy) does not support "depends_on" - blocking until the state you desire is reached.
- https://github.com/vegardit/await.sh
- `docker inspect lepp_php-fpm`
- `docker service inspect lepp_php-fpm`
- `docker service ls --format '{{.ID}} {{.Name}}' | grep ${serviceName}`
- If this command returns something there is a container running with your new image:
    - `docker service ps ${ServiceId} --format '{{.CurrentState}} {{.Image}}' | grep Running.*${newImageName}`

- NEW The task was initialized
- PENDING Resources for the task were allocated
- ASSIGNED Docker assigned the task to nodes
- ACCEPTED The task was accepted by a worker node. If a worker node rejects the task, the state changes to REJECTED
- PREPARING Docker is preparing the task
- STARTING Docker is starting the task
- RUNNING The task is executing
- COMPLETE The task exited without an error code
- FAILED The task exited with an error code
- SHUTDOWN Docker requested the task to shut down
- REJECTED The worker node rejected the task
- ORPHANED The node was down for too long
