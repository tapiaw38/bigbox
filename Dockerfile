FROM python:3.9.5 AS base

ENV PYTHONDONTWRITEBYTECODE=1
ENV POETRY_VIRTUALENVS_CREATE=false

RUN apt-get update -y&&\
    apt-get install nano -y && \ 
    apt-get clean

RUN pip install poetry

WORKDIR /app
COPY pyproject.toml poetry.lock ./
RUN poetry install --no-root --no-dev


COPY ./entrypoint.sh /entrypoint.sh


COPY ./ .

RUN chmod +x /entrypoint.sh


# run gunicorn
CMD gunicorn bigbox.config.wsgi:application --bind 0.0.0.0:$PORT
