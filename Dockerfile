#FROM python:3.6
FROM python:3.6-alpine

COPY requirements.txt /
RUN pip3 install --no-cache-dir -r /requirements.txt

COPY cowsay /cowsay
WORKDIR /
EXPOSE 8000

CMD gunicorn cowsay.app:app --bind=0.0.0.0 --workers=1 --log-file -