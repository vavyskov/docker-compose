# Locust

Zátěžové testování

## Testovací scénář (klikáním)

Postup vytvoření testovacího scénáře:

1. Firefox -> DevTools -> Network -> Network settings -> Persist Logs: **Yes**
2. Přejít na požadovanou URL např. https://docs.locust.io
3. "Naklikat" požadované chování
4. Firefox -> DevTools -> Network -> Network settings -> Save All As HAR

Vytvoření převodníku:

```
docker build -t har2locust .
```

Převod souboru z formátu HAR na PY:

```
docker run --rm -v $(pwd)/scenario:/tmp har2locust /tmp/docs.locust.io.har > scenario/docs.locust.io.py
```

```
docker run --rm -v $(pwd)/scenario:/tmp har2locust /tmp/www.google.com.har > scenario/www.google.com.py
```

## Testovací scénář (python)

Vytvořte soubor např. locustfile.py obsahující požadovaný testovací scénář:

```
from locust import HttpUser, between, task


class WebsiteUser(HttpUser):
    wait_time = between(5, 15)
    
    def on_start(self):
        self.client.post("/login", {
            "username": "test_user",
            "password": ""
        })
    
    @task
    def index(self):
        self.client.get("/")
        self.client.get("/static/assets.js")
        
    @task
    def about(self):
        self.client.get("/about/")
```

Více viz [Your first test](https://docs.locust.io/en/stable/quickstart.html)

## Testování

Spuštění zátěžového testu:

1. V souboru `.env` nastavte požadovnou URL adresu a příslušný testovací scénář.
2. Spusťte testovací prostředí (dle náročnosti odhadněte požadovaný počet "workerů"):
   ```
   docker-compose up -d --scale worker=2
   ```
3. Přejděte do grafického rozhraní na URL http://localhost:8089/
4. Spusťte zátěžový test

Zastavení zátěžového testu:

1. Přejděte do grafického rozhraní na URL http://localhost:8089/
2. Zastavte zátěžový test
3. Zastavte testovací prostředí:
   ```
   docker-compose down
   ```
