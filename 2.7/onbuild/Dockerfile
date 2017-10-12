FROM python:2.7-slim

ENV PYTHONPATH /app/src

RUN apt-get -y update && \
    apt-get -y install \
            gcc \
            git \
            mercurial \
            zip

COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt
RUN mkdir -p /app/src
COPY run.py /app

ONBUILD COPY ./src /app/src
ONBUILD COPY dev-requirements.txt /tmp/
ONBUILD COPY requirements.txt /tmp/
ONBUILD RUN pip install -r /tmp/dev-requirements.txt

WORKDIR /app

CMD python run.py
