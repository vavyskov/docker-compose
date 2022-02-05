# HAProxy

Each "project" must be added to the file `config/haproxy.cfg` e.g.:

```
frontend https
    ...
    acl project hdr(host) -i project.example.com
    use_backend project if project
    ...
```

```
backend project
    server project project_nginx:443 check ssl verify none
```

Statistics report is available on URL `http://127.0.0.1:1936/haproxy/stats`:
- User: admin
- Password: admin

Allows you to create and renew Let's Encrypt certificates.