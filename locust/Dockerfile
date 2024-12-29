FROM python:3.13.1-alpine

RUN apk add --no-cache build-base libffi-dev \
   && pip install --no-cache-dir har2locust \
   && apk del build-base libffi-dev

ENTRYPOINT ["har2locust"]
