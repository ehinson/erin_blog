# To start

`source venv/bin/activate`

`flask run`

## Be sure to start Postgres

 `pg_ctl -D /usr/local/var/postgres start`

## Be sure to start Elasticsearch

 `elasticsearch`

[SQLAlchemy documentation](https://flask-sqlalchemy.palletsprojects.com/en/2.x/api/#flask_sqlalchemy.SQLAlchemy)

[Elasticsearch documentation](https://elasticsearch-py.readthedocs.io/en/master/)

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