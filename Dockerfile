FROM python:3.9-buster

RUN pip install pipenv

WORKDIR /usr/src/app

CMD tail -f > /dev/null

