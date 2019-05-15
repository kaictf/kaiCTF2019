FROM python:3.7-alpine

LABEL name="backdoor-task"

RUN pip install Flask

WORKDIR /app

COPY . /app

ENTRYPOINT [ "python3" ]
CMD [ "app.py" ]

EXPOSE 80