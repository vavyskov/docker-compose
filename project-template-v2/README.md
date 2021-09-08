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
