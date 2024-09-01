FROM python:3.12-alpine

WORKDIR /django_service

ENV PYTHONUNBUFFERED=1

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
