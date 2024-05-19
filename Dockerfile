FROM python:3.12.3-slim

WORKDIR /var/app

COPY conf/requirements.txt .

RUN apt-get update && apt-get upgrade -y \
    && apt-get -y install default-libmysqlclient-dev gcc pkg-config \
    && pip install --no-cache-dir -r requirements.txt \
    && apt-get clean

COPY . .

WORKDIR /var/app/wallet_api

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

EXPOSE 8000

CMD ["sh", "-c", "gunicorn --bind 0.0.0.0:8000 wallet_api.wsgi:application"]
