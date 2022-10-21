# syntax=docker/dockerfile:1

FROM python:3.9
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN python --version | xargs echo
RUN pip install -r requirements.txt
COPY . /app