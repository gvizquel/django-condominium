# django-condominium #

Software for the management of communities organized in self-managed condominiums or not

## Docker
See installation instructions at: [docker documentation](https://docs.docker.com/compose/)

## Docker Compose
Install docker compose, see installation instructions at https://docs.docker.com/compose/install/

## Django
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
## Build images:

    $ docker-compose build
    $ docker-compose build --no-cache       # build without cache
    
## Fire it up
Start the container by issuing one of the following commands:

    $ docker-compose up             # run in foreground
    $ docker-compose up -d          # run in background
    $ docker-compose start          # run in background
    
## Stop processes:
    $ docker-compose stop          # run in background
    
Other commands
## See processes:

    $ docker-compose ps                 # docker-compose processes
    $ docker ps -a                      # docker processes (sometimes needed)
    $ docker stats [container name]     # see live docker container metrics
## See logs:

# See logs of all services
    $ docker-compose logs

# See logs of a specific service
    $ docker-compose logs -f [service_name]
Run commands in container:

Remove all docker containers:

    docker rm $(docker ps -a -q)
Remove all docker images:

    docker rmi $(docker images -q)
Some commands for managing the webapp
To initiate a command in an existing running container use the docker exec command.

# create migration file for an app
    $ docker exec -ti [container-name] python /code/manage.py makemigrations

# migrate
    $ docker exec -ti [container-name] python /code/manage.py migrate
