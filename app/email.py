from threading import Thread
from flask import render_template, current_app
from flask_mail import Message
from flask_babel import _
from app import mail

def send_async_email(app, msg):
  with app.app_context():
    mail.send(msg)

def send_email(subject, sender, recipients, text_body, html_body, attachments=None, sync=False):
  msg = Message(subject, sender=sender, recipients=recipients)
  msg.body = text_body
  msg.html = html_body
  if attachments:
    for attachment in attachments:
      # attach args: the filename, the media type, and the actual file data
      # if you have a list or tuple with arguments that you want to send to a function,
      # you can use func(*args) to have that list expanded into the actual argument list,
      # instead of having to use a more tedious syntax such as func(args[0], args[1], args[2])
      # (like javascript rest operator)
      msg.attach(*attachment)
  if sync:
    mail.send(msg)
  else:
    Thread(target=send_async_email, args=(current_app._get_current_object(), msg)).start()
