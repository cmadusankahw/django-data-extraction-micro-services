FROM python:3.7
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY requirements.txt /app/requirements.txt

RUN apt-get update && apt-get install -y libsasl2-modules libsasl2-dev
RUN pip install -r requirements.txt
COPY . /app