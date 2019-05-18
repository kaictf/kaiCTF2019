FROM python:3.7-alpine

LABEL name="history-task"

RUN pip install Flask

WORKDIR /app

COPY . /app

EXPOSE 80

ENTRYPOINT [ "python3" ]
CMD [ "app.py" ]