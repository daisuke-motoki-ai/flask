# Use the official lightweight Python image.      
# https://hub.docker.com/_/python
FROM python:3.7-slim

ENV APP_PATH /app
ENV FLASK_PATH ${APP_PATH}/flaskr
ENV TEST_PATH ${APP_PATH}/tests

WORKDIR ${APP_PATH}
RUN mkdir ${FLASK_PATH}
RUN mkdir ${TEST_PATH}


# apt-get による環境構築
RUN apt-get update
RUN apt-get -y install \
    build-essential \
    libpoppler-cpp-dev \
    pkg-config \
    python-dev \
    git

# pip module の構成に必要なファイルを転送
COPY .env .
COPY setup.py .

# 自作pip module の構築
RUN yes | pip install --upgrade pip
COPY flaskr/__init__.py ./flaskr/

# python file を転送
ENV  FLASK_APP flaskr
RUN python setup.py build
RUN python setup.py install

COPY flaskr/*.py ./flaskr/
