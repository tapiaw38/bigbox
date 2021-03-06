FROM python:3.8 AS base

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


EXPOSE 8000
ENTRYPOINT ["/entrypoint.sh"]

CMD gunicorn config.wsgi --bind 0.0.0.0:$PORT --chdir=/app
