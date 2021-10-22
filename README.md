# Big Box Challenge

## Local installation

### Create database in postgreSQL

PostgreSQL

POSTGRES_HOST=127.0.0.1
POSTGRES_PORT=5432
POSTGRES_DB=bigbox
POSTGRES_USER=postgres
POSTGRES_PASSWORD=1234

### Installing this repo with git:

console
foo@bar:~$ git clone https://github.com/tapiaw38/bigbox.git
Go inside downloaded repo and running poetry to install dependences
console
foo@bar:~$ poetry install

### Create migrations:

console
foo@bar:~$ python3 manage.py makemigrations

### Create relation in DB:

console
foo@bar:~$ python3 manage.py migrate

### Running Server:

console
foo@bar:~$ python3 manage.py runserver
