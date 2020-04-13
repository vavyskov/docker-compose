# Visualizer

This is only a sample app meant for learning Docker Swarm.

> Running Visualizer in production is **insecure** and should be avoided!

Use [portainer.io](https://www.portainer.io/) instead.

## Quick start (docker-compose)
1. Clone or download this repository
1. Go inside of directory `cd docker-compose/visualizer`
1. Run command:
    - Docker:

          docker network create frontend_network; \
          docker-compose up -d

    - Docker Swarm

          docker network create --driver=overlay frontend_network; \
          docker stack deploy --compose-file=docker-compose.yml visualizer


## Access to Visualizer: 
- **URL:** `http://localhost:9003` (Docker Toolbox: `192.168.99.100:9003`)
- **User:** `visualizer`
- **Password:** `visualizer`