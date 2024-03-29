# Project TEMPLATE

Content:
- Linux
- (E)Nginx
- MySQL/MariaDB
- PostgreSQL
- PHP
- Mailcatcher
- Adminer

## Quick start (docker-compose)

1. Clone or download this repository.
2. Go inside of directory `cd docker-compose/project-template/manually/docker`
3. Upravte `.env` dle potřeb (`.env` nefunguje ve Swarm módu).
4. Linux:
   - Run command `sh project_up.sh` (Docker).
   - Run command `sh stack-deploy_project.sh` (Docker Swarm).
5. Other systems:
   - (Příkazem `docker-compose config` si zobrazte výslednou konfiguraci.)
   - (Zobrazený výstup si uložte do nového projektu jako `docker-compose.yml` a upravte dle potřeb.)
   - Run command:
       - Docker:

             docker-compose pull

             docker network create frontend_network
             docker network create mailcatcher_network
             docker network create adminer_network
             docker network create project_network
             docker-compose up -d

             docker-compose stop
             docker-compose down

       - Docker Swarm

             docker-compose pull
          
             docker network create --driver=overlay frontend_network
             docker network create --driver=overlay mailcatcher_network
             docker network create --driver=overlay adminer_network
             docker network create --driver=overlay project_network
             docker stack deploy --compose-file=docker-compose.yml project
             docker stack deploy --compose-file=docker-compose.override.yml project
          
             docker stack rm project

## URL

- project.example.com
- project.example.com/adminer | adminer.example.com
- mailcatcher.example.com

## Notes

Volitelně spusťte:
- mkcert + nginx-proxy
- (traefik)

## Aktualizace docker obrazů

1. `docker-compose pull`
2. `docker-compose up -d` nebo `docker stack daploy...`

## ToDo

- autogenerator
  - envsubst (project-create.sh)
- Docker Secrets: http://blog.code4hire.com/2018/06/the-rabbit-hole-is-deep-when-trying-to-switch-from-environment-variables-file-to-docker-secrets/
- docker-share (sdílení společného nastavení "project mode ???", "php.ini", "PHP extensions" mezi kontejnery PHP-FPM a SSH-PHP-CLI)
    - https://github.com/paslandau/docker-php-tutorial/blob/part_3_structuring-the-docker-setup-for-php-projects/.docker/.shared/scripts/install_php_extensions.sh
    - https://github.com/mlocati/docker-php-extension-installer/
- Mailcatcher: project.example.com/mailcatcher
- Docker Config

## Testy

Sendmail (webové prostředí + SSH klient):
- `echo -e "Subject: Testing" | msmtp --debug -t user@domain.com`
- `echo -e "Subject: Test Mail\r\n\This is a test mail. Did you receive an email?" | msmtp --debug --from from@yourdomain.com -t to@someone.com`
- `php -r "mail('to@domain.com','Test Mail from PHP', 'This is a test mail from PHP. Did you receive an email?', 'From: from@domain.com');"`

Kontrola požadavků:
- `wp package install git@github.com:johnbillion/ext.git`
    - `wp ext check` (OK)
- `drupal check` (OK)
- `symfony check:requirements` (OK)

Testované položky:

1. instalace
1. status
1. instalace rozšíření (z webového prostředí + terminálu)
1. vložení obrázku (velikost > 5 MB a rozlišení > 2000 px)
1. generování náhledů obrázků
1. online úprava obrázků
1. aktualizace (z webového prostředí + terminálu)
1. odeslání e-mailu (např. požadavek na obnovu hesla)

Statické stránky:
- funkčnost více HTML souborů v různých adresářích
- sending e-mails (Docker Toolbox, SMTP port 1025): OK

Wordpress ručně:
- `wget https://cs.wordpress.org/latest-cs_CZ.zip`
- proxy vyžaduje ruční konfiguraci:
    - wp-config.php
        - `define('WP_PROXY_HOST', 'proxy.example.com');`
        - `define('WP_PROXY_PORT', '8080');`
        - `define('WP_PROXY_USERNAME', 'user');`
        - `define('WP_PROXY_PASSWORD', 'password');`
        - (`define('WP_PROXY_BYPASS_HOST', '*.wordpress.org');`)
- řazení v databázi vyžaduje ruční konfiguraci:
    - wp-config.php
        - (`define('DB_CHARSET', 'utf8mb4');` - autodetekce je OK)
        - `define('DB_COLLATE', 'utf8mb4_czech_ci');` - autodetekce WP verze 5.4 NEFUNGUJE
- sending e-mails (Docker Toolbox, SMTP port 1025): OK
- vše ostatní OK

Wordpress - cli:
- stažení WP OK

Drupal - ručně:
- `wget https://www.drupal.org/download-latest/zip`
- ??? status - aby bylo vše OK, je třeba vysypat cache (nebo přejít na adresu /update.php/selection)
- sending e-mails (Docker Toolbox, SMTP port 1025):
    - Drupal 7 require module https://www.drupal.org/project/smtp (set Server and Port): OK
    - Drupal 9: how to correctly install module https://www.drupal.org/project/smtp (missing phpmailer/phpmailer) ???
- vše ostatní OK

Drupal - composer (docker-machine minimálně 2G RAM)
- `cd; drupal site:new` [drupal-composer, html]
    - `composer install`
    - instalace rozšíření "OK" - současnou chybu verze Drupal 8.8.5 je možné vyřešit viz níže :(
        - https://www.drupal.org/docs/develop/using-composer/starting-a-site-using-drupal-composer-project-templates#s-workaround
        - dočasně v sites/default/settings.local.php (sites/default/settings.php) odkomentujte (vložte) řádek:
            - `$settings['skip_permissions_hardening'] = TRUE;`
    - sending e-mails (Docker Toolbox, SMTP port 1025): ???
    - vše ostatní OK
- `cd; composer create-project drupal/recommended-project:9.1.0 html --no-install; cd html; composer install`
    - ???
    - sending e-mails (Docker Toolbox, SMTP port 1025): Drupal 9 require module https://www.drupal.org/project/smtp (set Server and Port): OK
- (`cd; composer create-project drupal-composer/drupal-project:8.x-dev html --no-interaction; cd html; composer install`)
    - instalace rozšíření "OK" - současnou chybu verze Drupal 8.8.5 je možné vyřešit viz níže :(
        - https://www.drupal.org/docs/develop/using-composer/starting-a-site-using-drupal-composer-project-templates#s-workaround
        - dočasně v sites/default/settings.local.php (sites/default/settings.php) odkomentujte (vložte) řádek:
            - `$settings['skip_permissions_hardening'] = TRUE;`
    - sending e-mails (Docker Toolbox, SMTP port 1025): ???
    - vše ostatní OK
- `cd; drupal quick:start` [drupal-composer, html, standard] - spouští vlastní server...
    - !!! nefunguje

Symfony - symfony:
- `symfony new --full html`
- instalace OK
- další položky ???

Moodle - ručně:
- `wget https://download.moodle.org/download.php/direct/stable39/moodle-latest-39.zip`
    - odkazy uvedené na https://download.moodle.org/releases/latest/ není možné pro stažení z terminálu (wget, curl) použít - stažené archivy nejsou kompletní :( 

Možnost aktualizace CLI nástrojů z SSH-PHP-CLI?
- wp cli update (permission denied)
- drupal self-update (permission denied)
- symfony self-update (?)
- composer self-update (?)

Docker
- `docker stats` (Ctrl+C - exit)
- `docker stats project_ssh`

Docker Toolbox
- Memory
    - `VBoxManage showvminfo default | grep Memory` | `docker-machine ssh default free` | `docker-machine inspect`
        - změna výchozího nastavení
            - `~/.docker/machine/machines/default/config.json` | `~/.docker/machine/default/config.json`
        - konfigurace stávajícího:
            - `docker-machine stop default`
              `VBoxManage modifyvm default --memory 4096` (min. 2048)
              `docker-machine start default`
        - vytvoření nového
            - `docker-machine create -d virtualbox --virtualbox-memory 4096 default`
            - `docker-machine create -d virtualbox --virtualbox-memory=4096 --virtualbox-cpu-count=2 --virtualbox-disk-size=50000 default`

Při běhu v dynamickém prostředí je zvykem aplikace monitorovat, často nástrojem [Prometheus](https://prometheus.io/docs/introduction/overview/).
