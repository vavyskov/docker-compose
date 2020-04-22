# docker-compose

This git repository allows you to run defined applications in Docker or Docker Swarm mode.

## Requirements:
1. [Docker CE](https://download.docker.com?target=_blank) or [Docker Toolbox](https://github.com/docker/toolbox/releases/?target=_blank) (Virtualbox)
    - `docker`
    - `docker-compose`
1. [Git](https://git-scm.com/?target=_blank) (optional)
    - `git`

## Docker Swarm (optional)

- Docker CE:

      docker swarm init

- Docker Toolbox:

      docker swarm init --advertise-addr 192.168.99.100

## Notes

Stacks "whoami" and "stack-project-template" offer the most documentation.

## Commands

Show all used ports: 

    docker ps -q | xargs -n1 docker port | cut -d: -f2 | sort -n
    docker ps --format "table {{.ID}}\t{{.Names}}\t{{.Ports}}" -a
    docker ps -q | xargs -n 1 docker inspect -f '{{ .Name }} {{range $p, $conf := .NetworkSettings.Ports}} {{$p}}{{end}}' | sed 's#^/##'

Summary of the currently used space

    docker system df
    
Resource usage statistics

    docker stats

## ToDo

- otestovat změnu hesla u existujících databází (případně i změnu uživatele a název databáze)
- project-delete.sh
- stack-project-tamplate/stack-lemp
- stack-standalone
- selenium
- [healthcheck](https://docs.docker.com/engine/reference/builder/#healthcheck)