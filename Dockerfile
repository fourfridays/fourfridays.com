# <WARNING>
# Everything within sections like <TAG> is generated and can
# be automatically replaced on deployment. You can disable
# this functionality by simply removing the wrapping tags.
# </WARNING>

FROM python:3.9.7-slim-bullseye

# <NPM>
# </NPM>

# <BOWER>
# </BOWER>

RUN apt-get update \
    # lipq-dev and gg for psycopg2 build
    && apt-get install -y libpq-dev gcc libjpeg62-turbo-dev zlib1g-dev libwebp-dev \
    && pip install pip-tools==5.5.0 \
    && pip install start==0.2


# set the working directory
WORKDIR /app
# copy the repository files to it
COPY . /app

COPY requirements.* /app/
COPY addons-dev /app/addons-dev/
RUN pip install -r requirements.txt

RUN python manage.py collectstatic --noinput

EXPOSE 80
CMD uwsgi --http=0.0.0.0:80 --module=wsgi