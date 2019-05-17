FROM tiangolo/uwsgi-nginx-flask:python3.7

RUN apt-get update && apt-get install -y curl wget

COPY ./app /app

EXPOSE 80