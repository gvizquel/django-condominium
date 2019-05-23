FROM python:3.7

ENV PYTHONUNBUFFERED 1
ENV DJANGO_ENV dev
ENV DOCKER_CONTAINER 1

RUN pip install --upgrade pip

COPY . /code/
WORKDIR /code/

RUN pip install pipenv
RUN pipenv install --system

CMD python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000