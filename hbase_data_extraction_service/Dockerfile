FROM python:3.7
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN apt-get update && apt-get install libsasl2-dev
RUN pip install -r requirements.txt
COPY . /app