FROM python:3.6.5-alpine3.7

COPY requirements.txt /

RUN pip3 install -r /requirements.txt

ARG service
COPY $service/ /$service

ARG service
WORKDIR /$service

CMD["behave"]
