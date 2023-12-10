FROM python:3.10-slim-buster

RUN apt-get update && apt-get install -y gcc libssl-dev libffi-dev libpq-dev

WORKDIR /doc-company-ai

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . .

RUN pip install -r requirements.txt
