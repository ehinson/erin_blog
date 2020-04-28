# To start

`source venv/bin/activate`

`flask run`

## Be sure to start Postgres:

 `pg_ctl -D /usr/local/var/postgres start`

[SQLAlchemy documentation](https://flask-sqlalchemy.palletsprojects.com/en/2.x/api/#flask_sqlalchemy.SQLAlchemy)

## To run a local SMTP server

```python
export FLASK_DEBUG=0
export MAIL_SERVER=localhost
export MAIL_PORT=8025
```

`python -m smtpd -n -c DebuggingServer localhost:8025`

## Based on

[The Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)

## Internationalization:
`flask translate init LANG` to add a new language
`flask translate update` to update all the languages after making changes to the _() and _l() language markers
`flask translate compile` to compile all languages after updating the translation files