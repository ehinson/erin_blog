from app import create_app, db, cli
from app.models import User, Post, Notification, Message, Task

app = create_app()
cli.register(app)

@app.shell_context_processor
# added models to the shell context, to make them accessible in shell sessions without having to import them
def make_shell_context():
  return {'db': db, 'User': User, 'Post': Post, 'Message': Message, 'Notification': Notification, 'Task': Task}
