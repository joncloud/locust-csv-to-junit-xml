FROM python:3.9-buster

WORKDIR /app
COPY requirements.txt ./
RUN pip install -r ./requirements.txt

COPY prep.sh ./
COPY unittest.cfg ./
COPY *.py ./

RUN ./prep.sh

RUN nose2 -v --config ./unittest.cfg main_test
