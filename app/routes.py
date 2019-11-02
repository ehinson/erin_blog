from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Erin'}
    posts = [
        {
            'author': user,
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': user,
            'body': 'Beautiful day in Fort Collins!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
