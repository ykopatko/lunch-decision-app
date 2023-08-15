FROM python:3.11.1-slim-buster
LABEL mainteiner="cs.kopatko.evgen@gmail.com"

ENV PYTHONUNBUFFERED 1

WORKDIR app/

COPY requirements.txt requirements.txt


RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*


RUN pip install -r requirements.txt

COPY . .

RUN adduser --disabled-password --no-create-home django-user
RUN mkdir -p /vol/web/media
RUN chown -R django-user:django-user /vol/
RUN chmod -R 755 /vol/web/

USER django-user
