FROM python:3.9.5-buster

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN apt update && apt install nano

CMD ["gunicorn", "-b", "0.0.0.0:42080", "--certfile", "cert.pem", "--keyfile", "key.pem", "--workers", "2", "app:app"]