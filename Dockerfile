FROM python:3.11-slim-bullseye

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERRED 1

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

