<<<<<<< HEAD
from threading import Thread
=======
>>>>>>> bd5a3542950f6ef5354a81d825cfe6c8f322db79
from flask import render_template
from flask_mail import Message
from app import app, mail

<<<<<<< HEAD

def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)

=======
>>>>>>> bd5a3542950f6ef5354a81d825cfe6c8f322db79
def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
<<<<<<< HEAD
    Thread(target=send_async_email, args=(app, msg)).start()
=======
    mail.send(msg)
>>>>>>> bd5a3542950f6ef5354a81d825cfe6c8f322db79

def send_password_reset_email(user):
    token = user.get_reset_password_token()
    send_email('[Microblog] Reset Your Password',
                sender=app.config['ADMINS'][0],
                recipients=[user.email],
                text_body=render_template('email/reset_password.txt',
                                         user=user, token=token),
                html_body=render_template('email/reset_password.html',
                                          user=user, token=token))