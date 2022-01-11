# PROJECT template

Často používané "docker" příkazy:

    sh project_up.sh

    docker exec -it <container-id> sh
      exit

    sh project_down.sh

Často používané "swarm" příkazy:

    sh stack_deploy.sh

    docker service ls
    docker stack ls

    sh stack_rm.sh

- Swarm nepodporuje `.env`, ale je možné to "obejít" pomocí "docker-copmpose config"
- Swarm nepodporuje `depends_on`, ale je možné to "obejít" postupným spuštěním
- Swarm vyžaduje URL `127.0.0.1` (`localhost` nefunguje)

## Access to project:
- **URL:** `http://localhost:8088` (Docker Toolbox: `192.168.99.100:8088`)

## Configure your system `hosts` file:

- `127.0.0.1 project.example.com` (Docker CE)
- `192.168.99.100 project.example.com` (Docker Toolbox)

Path:
- Linux: `/etc/hosts`
- macOX: `/private/etc/hosts`
- Windows: `C:\Windows\System32\drivers\etc\hosts`

## Adding trusted root certificate authority
1. Operating system
    - **Linux (Debian)**:

          sudo cp rootCertificateAuthority.crt /usr/local/share/ca-certificates/
          sudo update-ca-certificates

2. Browsers:
    - **Chrome**: Settings -> Privacy and security -> Security -> Manage certificates -> Authorities -> Import (rootCertificateAuthority.crt)

## Kontrola

1. Git:
   - stažení repozitáře (HTTPS)
     - [ ] dev
     - [x] prod
     - swarm
       - [ ] prod
   - stažení repozitáře (SSH)
     - [ ] dev
     - [x] prod
     - swarm
       - [ ] prod
2. Funkční odesílání pošty:
    - docker
        - [ ] dev (mailcatcher)
        - [x] prod (mailcatcher)
        - [ ] prod
    - swarm
        - [ ] prod
3. ...
