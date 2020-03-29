Logbook
=======

Setup
-----
Install deps with pipenv

Clone env.ini.dist into env.ini and set your database settings there

~/.ssh/config
-----------
```
Host github.com
IdentityFile ~/.ssh/github
```

Fabric deployment
-----------------
pipenv run fab --list
pipenv run fab --help deploy

Systemd
-------
/etc/systemd/system/logbook.service
```
[Unit]
Description=uvicorn server for logbook
After=network.target

[Service]
User=web
Group=nginx
ExecStart=/path/to/logbook/uvicorn.sh
```

Nginx
-----
```
server {
    server_name logbook.com
    listen 80;

    access_log  /var/log/nginx/logbook.access.log;
    error_log  /var/log/nginx/logbook.error.log;

    location / {
      proxy_set_header X-Forwarded-Host $host;
      proxy_set_header X-Forwarded-Server $host;
      proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
      proxy_set_header X-Forwarded-Proto $scheme;
      proxy_pass http://127.0.0.1:8002;
    }

    location /static {
        alias /path/to/logbook/static/;
    }

    location /media {
        alias /path/to/logbook/media/;
    }    
}
```

Docker
------
Running mysql container
```shell
docker run --name mysql-portfolio -p 3306:3306 -e MYSQL_ROOT_PASSWORD=root -e MYSQL_DATABASE=portfolio -d mysql:latest
```
