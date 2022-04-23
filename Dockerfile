FROM python:3.10.4-alpine

WORKDIR /code

COPY . /code/

RUN apk add --no-cache --upgrade --virtual .build-deps \
    gcc \
    linux-headers \
    musl-dev \
    libxml2-dev \
    libxslt-dev \
    && pip3.10 install -U pip setuptools \
    && pip install --no-cache-dir -r requirements.txt \
    && apk del --no-cache .build-deps

RUN apk add libxml2 libxslt # Runtime SO dependencies