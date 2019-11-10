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
