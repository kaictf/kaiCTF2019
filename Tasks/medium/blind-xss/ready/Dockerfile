FROM python:3.7-alpine

LABEL name="blind-xss-task"

# Installs latest Chromium package.
RUN echo @edge http://nl.alpinelinux.org/alpine/edge/community >> /etc/apk/repositories \
    && echo @edge http://nl.alpinelinux.org/alpine/edge/main >> /etc/apk/repositories \
    && apk add --no-cache \
    chromium@edge \
    harfbuzz@edge \
    nss@edge \
    freetype@edge \
    ttf-freefont@edge \
    && pip install Flask \
    && rm -rf /var/cache/* \
    && mkdir /var/cache/apk

COPY app.py app.py

ENTRYPOINT [ "python3" ]
CMD [ "app.py" ]