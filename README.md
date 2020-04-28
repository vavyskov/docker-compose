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

List all containers in a user-defined docker network e.g. "frontend_network"?

    docker network inspect frontend_network | grep Name | tail -n +2 | cut -d':' -f2 | tr -d ',"'
    docker inspect -f '{{json .Containers}}' frontend_network | python -m json.tool

List all used ports (it does not work in Swarm mode): 

    docker container ls -q | xargs -n1 docker port | cut -d: -f2 | sort -n
    docker container ls --format "table {{.ID}}\t{{.Names}}\t{{.Ports}}" -a
    docker container ls -q | xargs -n 1 docker inspect -f '{{ .Name }} {{range $p, $conf := .NetworkSettings.Ports}} {{$p}}{{end}}' | sed 's#^/##'

Summary of the currently used space

    docker system df
    
Resource usage statistics

    docker stats

## ToDo

- hostname (identifikace kontejneru např. při SSH přístupu)
- SSH command history - volume
- For better performances, you should move the cache and log directories to a non-shared folder of the VM.
- otestovat změnu hesla u existujících databází (případně i změnu uživatele a název databáze)
- project-template/project-delete.sh
- project-standalone
- project-lemp
- Middlewares Prefix (/adminer, /pgadmin, /mailcatcher)
- selenium
- [healthcheck](https://docs.docker.com/engine/reference/builder/#healthcheck)