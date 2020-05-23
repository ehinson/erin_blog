# To start

## Install Python 3 and dependencies

```bash
brew install python

OR

brew update
brew upgrade python3

```

## Run the project

`virtualenv venv`

`source venv/bin/activate`

`pip install -r requirements.txt`

`flask run`

## Be sure to start Postgres!

 `pg_ctl -D /usr/local/var/postgres start`

## Be sure to [install](https://www.elastic.co/guide/en/elasticsearch/reference/7.7/brew.html) and start Elasticsearch!

`brew tap elastic/tap`

`brew install elastic/tap/elasticsearch-full`

`elasticsearch`

## Be sure to start Redis Server!

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

## To start the shell with the application context

`flask shell`

## Running migrations

Generate a new migration

`flask db migrate -m "migration message"`

Apply it to the database

`flask db upgrade`

## To start the shell with the "python" command, you will need to import the current_app

If you see the dreaded "RuntimeError: Working outside of application context." error:

```python
>>> from app import create_app
>>> app = create_app()
>>> app.app_context().push()
>>> current_app.config['SQLALCHEMY_DATABASE_URI']
'sqlite:////your/cool/uri'
```

## To run a local SMTP server

```python
export FLASK_DEBUG=0
export MAIL_SERVER=localhost
export MAIL_PORT=8025
```

`python -m smtpd -n -c DebuggingServer localhost:8025`

## Based on

[The Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)

## Internationalization

`flask translate init LANG` to add a new language

`flask translate update` to update all the languages after making changes to the _() and _l() language markers

`flask translate compile` to compile all languages after updating the translation files