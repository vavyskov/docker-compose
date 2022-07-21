# Docker Environment

## Environments

Change `.env` as needed.

## Quick start
1. Clone or download this repository
2. Go inside of directory `cd project-environment`
3. Run commands:

          docker network create frontend_network backend_network database_network
          docker-compose up -d

## Adding trusted root certificate authority (e.g. from mkcert)
1. Operating system
   - **Windows**
     - double-click the file `project-environment/certificates/rootCA.crt` and install as root certificate authority:
       - local computer
       - custom location
         - trusted root certificate authority
   - **Linux (Debian)**:

         sudo cp rootCA.crt /usr/local/share/ca-certificates/
         sudo update-ca-certificates

2. Browsers:
   - **Chrome**: Settings -> Privacy and security -> Security -> Manage certificates -> Authorities -> Import (rootCA.crt)

## Configure your system `hosts` file:

- `127.0.0.1 traefik.example.com adminer.example.com mailcatcher.example.com`

Path:
- Linux: `/etc/hosts`
- macOX: `/private/etc/hosts`
- Windows: `C:\Windows\System32\drivers\etc\hosts`

## Access URLs:
- **Traefik:** `https://traefik.example.com`
- **Adminer:** `https://adminer.example.com`
- **Mailcatcher:** `https://mailcatcher.example.com`
