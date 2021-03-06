# To start

## Run the project

### Install Python 3 and dependencies

```bash
brew install python

OR

brew update
brew upgrade python3

```

`virtualenv venv`

`source venv/bin/activate`

`pip install -r requirements.txt`

### create an .env file from the .env.example file and your own values

```bash
DATABASE_URL="postgresql:///blog"
MAIL_SERVER= localhost
MAIL_PORT=8025
SECRET_KEY=a-really-long-and-unique-key-that-no-one-knows
ELASTICSEARCH_URL=http://localhost:9200
```

### Start the app

`flask run`

### Be sure to install and start Postgres!

`brew install postgresql`

To migrate existing data from a previous major version of PostgreSQL run:

`brew postgresql-upgrade-database`

To have launchd start postgresql now and restart at login:

`brew services start postgresql`

Or, if you don't want/need a background service you can just run:

`pg_ctl -D /usr/local/var/postgres start`


### Be sure to [install](https://www.elastic.co/guide/en/elasticsearch/reference/7.7/brew.html) and start Elasticsearch!

`brew tap elastic/tap`

`brew install elastic/tap/elasticsearch-full`

`elasticsearch`

### Be sure to start Redis Server!

`brew update`

`brew install redis`

To have launchd start redis now and restart at login:
```
brew services start redis
```

to stop it, just run:

```
brew services stop redis
```

Or, if you don't want/need a background service you can just run:

```
redis-server /usr/local/etc/redis.conf
```

[SQLAlchemy documentation](https://flask-sqlalchemy.palletsprojects.com/en/2.x/api/#flask_sqlalchemy.SQLAlchemy)

[Elasticsearch documentation](https://elasticsearch-py.readthedocs.io/en/master/)

[Redis documentation](http://redis.io)

### To start the shell with the application context

`flask shell`

## Running [migrations](https://flask-migrate.readthedocs.io/en/latest/)

Create an `env.py` file from the example in the migrations folder

If `flask db migrate` fails, try to delete the latest migration file ( a python file) then try to perform a migration afresh.

If issue still persists try these commands :

```bash
flask db stamp head  # To set the revision in the database to the head, without performing any migrations. You can change head to the required change you want.
flask db migrate     # To detect automatically all the changes.
flask db upgrade     # To apply all the changes.
```

Generate a new migration

`flask db migrate -m "migration message"`

Apply it to the database

`flask db upgrade`

### To start the shell with the "python" command, you will need to import the current_app

If you see the dreaded "RuntimeError: Working outside of application context." error:

```python
>>> from app import create_app
>>> app = create_app()
>>> app.app_context().push()
>>> current_app.config['SQLALCHEMY_DATABASE_URI']
'sqlite:////your/cool/uri'
```

### To run a local SMTP server

```python
export FLASK_DEBUG=0
export MAIL_SERVER=localhost
export MAIL_PORT=8025
```

`python -m smtpd -n -c DebuggingServer localhost:8025`

### Based on

[The Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)

### Internationalization

`flask translate init LANG` to add a new language

`flask translate update` to update all the languages after making changes to the _() and _l() language markers

`flask translate compile` to compile all languages after updating the translation files

## Postgres Commands

### Create database

```bash
createdb <database_name>
```

> `createdb my_database`

### List databases

```bash
psql -U postgres -l
```

### Show tables in database

```bash
psql -U postgres -d <database_name>
```

> `psql -U postgres -d my_database`

### Drop database

```bash
dropdb <database_name>
```

> `dropdb my_database`

### Restart database

```bash
dropdb <database_name> && createdb <database_name>
```

> `dropdb my_database && createdb my_database`
