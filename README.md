# To start

`source venv/bin/activate`

`flask run`

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

## To extract PyBabel texts to a file and create a Spanish translation:
`pybabel extract -F babel.cfg -k _l -o messages.pot .`
`pybabel init -i messages.pot -d app/translations -l es`

## To update texts in PyBabel:
`pybabel extract -F babel.cfg -k _l -o messages.pot .`
`pybabel update -i messages.pot -d app/translations`