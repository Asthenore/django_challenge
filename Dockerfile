FROM python:3.7-alpine
LABEL Erik Govea

ENV PYTHONBUFFERED 1

COPY ./requierements.txt ./requierements.txt
RUN pip install -r /requierements.txt
 
RUN mkdir /challenge
WORKDIR /challenge
COPY ./challenge /challenge

RUN adduser -D user
USER user