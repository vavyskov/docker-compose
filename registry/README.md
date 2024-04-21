# Registry

Distribuční registr

Vhodné pro interní vývojový pracovní postup

Dokumentace:
- [Registry](https://hub.docker.com/_/registry)
- [Distribution](https://distribution.github.io/distribution/)
- [Konfigurace produkce](https://distribution.github.io/distribution/about/configuration/)
    - [ochrana pomocí TLS](https://distribution.github.io/distribution/about/deploying/#run-an-externally-accessible-registry)
    - řízení přístupu

Spuštění:
```
docker compose up -d
```

Vypsání obsahu registru:
```
curl localhost:5000/v2/_catalog
```

Příklad vložní obrazu do registru:
```
docker pull nginx:latest
docker tag nginx:latest localhost:5000/my-nginx
docker push localhost:5000/my-nginx
```

Příklad použití obrazu z registru:
```
docker pull localhost:5000/my-nginx
```

Příklad odstranění obrazu:
```
docker image remove nginx:latest
docker image remove localhost:5000/my-nginx
```

Jak odstranit obrazu z registru ???
```
???
```

Zastavení registru:
```
docker compose down
```

Odstranění registru a všech jeho dat:
```
docker container rm --volumes registry
```
