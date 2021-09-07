#!/bin/sh

#docker network create --driver=overlay frontend_network
#docker network create --driver=overlay project_network

#docker stack deploy --compose-file=docker-compose.yml project
#docker stack deploy --compose-file=docker-compose.override.yml project

#docker stack deploy --compose-file <(docker-compose --file=docker-compose.yml config) project
#docker stack deploy --compose-file <(docker-compose config) project

## Part 1
docker-compose --file=docker-compose.yml config | docker stack deploy --compose-file - project
## Part 2 (depends on "Part 1")
## docker-compose config | docker stack deploy --compose-file - project
## Require remove "depends_on" section (https://unix.stackexchange.com/questions/648684/how-do-i-remove-all-specifc-sub-sections-of-a-specifc-header-in-a-yaml-file?rq=1#answer-650052)
docker-compose config | sed -e 'H;x;/^\(  *\)\n\1/{s/\n.*//;x;d;}' -e 's/.*//;x;/\depends_on/{s/^\( *\).*/ \1/;x;d;}' | docker stack deploy --compose-file - project