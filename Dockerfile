FROM python:3.11.8-slim-bookworm

RUN apt-get update \
    # lipq-dev and gg for psycopg2 build
    && apt-get install -y libpq-dev gcc libjpeg62-turbo-dev zlib1g-dev \
    libwebp-dev libffi-dev \
    && pip install --upgrade pip \
    && pip install pip-tools


# set the working directory
WORKDIR /app
# copy the repository files to it
COPY . /app

COPY requirements.* /app/

RUN pip install -r requirements.txt

RUN python manage.py collectstatic --noinput

EXPOSE 80

# GUNICORN
CMD ["gunicorn", "--bind", ":80", "--workers", "1", "--threads", "2", "--worker-class", "gevent", "--max-requests-jitter", " 2000", "--max-requests", "1500", "wsgi"]