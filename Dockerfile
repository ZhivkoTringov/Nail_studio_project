FROM python:3

ENV PYTHONDOWNWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt /app/

RUN pip install -r requirements.txt


COPY manage.py /app/manage.py
COPY staticfiles /app/staticfiles
COPY photos/photos /app/photos/photos
COPY templates /app/templates
COPY Nail_studio /app/Nail_studio
COPY tests /app/tests




