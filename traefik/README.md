# Traefik

## Environments
This Compose file contains the following environment variables:

- `COMPOSE_PROJECT_NAME` the default value is **traefik**
- `TRAEFIK_VERSION` the default value is **2.8**
- `TRAEFIK_PORT` the default value is **8080**

You can set environment variables in `.env` file.

## Quick start (docker-compose)
1. Clone or download this repository
2. Optionally run `mkcert` or place custom wildcard certificate in a directory:
   ```
   /etc/ssl/path/wildcard_example.com.crt
   /etc/ssl/path/wildcard_example.com.key
   ```
4. Go inside of the directory `cd docker-compose/traefik`
5. Run command:
    - Docker:

          docker network create frontend_network
          docker-compose up -d

    - Docker Swarm

          docker network create --driver=overlay frontend_network
          docker stack deploy --compose-file=docker-compose.yml traefik

## Quick start (docker)

    docker network create frontend_network; \
    docker run -itd \
        --name traefik \
        --publish 80:80 \
        --publish 443:443 \
        --publish 8080:8080 \
        --network frontend_network \
        traefik:v2.8

## Access to Traefik: 
- **URL:** `http://localhost:8080` (Docker Toolbox: `192.168.99.100:8080`)
- **User:** `traefik`
- **Password:** `traefik`

## Configure your system `hosts` file:

- `127.0.0.1 traefik.example.com` (Docker CE)
- `192.168.99.100 traefik.example.com` (Docker Toolbox)

Path:
- Linux: `/etc/hosts`
- macOX: `/private/etc/hosts`
- Windows: `C:\Windows\System32\drivers\etc\hosts`

## Adding trusted root certificate authority (e.g. from mkcert)
1. Operating system
   - **Linux (Debian)**:

         sudo cp rootCA.crt /usr/local/share/ca-certificates/
         sudo update-ca-certificates

2. Browsers:
   - **Chrome**: Settings -> Privacy and security -> Security -> Manage certificates -> Authorities -> Import (rootCA.crt)

## Custom certificates

Config folder with `dynamic.yml` file is the only available method to configure custom certificates!

## Network
Show IP address:

    docker network inspect frontend_network | grep IPv

## Let's Encrypt
[Traefik - Let's Encrypt](https://git-scm.com/?target=_blank)
