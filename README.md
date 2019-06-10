# django-condominium #

Software for the management of communities organized in self-managed condominiums or not

## Docker ##

See installation instructions at: [docker documentation](https://docs.docker.com/compose/)

## Docker Compose ##

Install docker compose, see installation instructions at https://docs.docker.com/compose/install/

## Django ##

Edit the settings.py file with the correct database credentials and static root:

    DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.postgresql_psycopg2',
          'NAME': 'postgres',
          'USER': 'postgres',
          'PASSWORD': 'postgres',
          'HOST': 'db',
          'PORT': '5432',
      }
    }

## Build images ##

```console
user@nombre_maquina:~$ docker-compose build
user@nombre_maquina:~$ docker-compose build --no-cache       # build without cache
```

## Fire it up ##

Start the container by issuing one of the following commands:

```console
user@nombre_maquina:~$ docker-compose up             # run in foreground
user@nombre_maquina:~$ docker-compose up -d          # run in background
user@nombre_maquina:~$ docker-compose start          # run in background
```

## Stop processes ##

```console
user@nombre_maquina:~$ docker-compose stop          # run in background
```

Other commands

## See processes ##

user@nombre_maquina:~$ docker-compose ps                 # docker-compose processes
user@nombre_maquina:~$ docker ps -a                      # docker processes (sometimes needed)
user@nombre_maquina:~$ docker stats [container name]     # see live docker container metrics

## See logs ##

# See logs of all services

user@nombre_maquina:~$ docker-compose logs

# See logs of a specific service

user@nombre_maquina:~$ docker-compose logs -f [service_name]
Run commands in container:

Remove all docker containers:

    docker rm $(docker ps -a -q)
Remove all docker images:

    docker rmi $(docker images -q)
Some commands for managing the webapp
To initiate a command in an existing running container use the docker exec command.

# create migration file for an app
user@nombre_maquina:~$ docker exec -ti [container-name] python /code/manage.py makemigrations

# migrate
user@nombre_maquina:~$ docker exec -ti [container-name] python /code/manage.py migrate

# django-condominium #

## Install ##

    Docker-Compose
    Docker-Machine

## Crea una maquina virtual ##

$ docker-machine create -d virtualbox dev;

The create command set up a new “Machine” (called dev) for Docker development. In essence, it started a VM with the Docker client running. Now just point Docker at the dev machine:

$ eval $(docker-machine env maquina-virtual)

Run the following command to view the currently running Machines:

$ docker-machine ls

$ docker-compose build
$ docker-compose up -d

docker-compose run condominium /usr/local/bin/python manage.py migrate

## Adicionales ##

tree -C -I 'bower*|autocomplete*|Leaflet*|css|js|admin|dist|plugins|*.json|*.png|*.jpg|*.html'

## Para conectarme a una imagen ##

docker exec -ti contenedor bash

