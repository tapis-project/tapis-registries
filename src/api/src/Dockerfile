FROM python:3.9

RUN apt-get clean

RUN apt-get update

RUN apt-get install -y vim

RUN mkdir src

COPY src/api/src/requirements.txt /src/requirements.txt

WORKDIR /src

RUN pip install -r requirements.txt

COPY src/api/src/ /src


