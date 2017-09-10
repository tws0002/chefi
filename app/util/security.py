# ourapp/util/security.py
from itsdangerous import URLSafeTimedSerializer
from flask_mail import Message
from .. import app,mail
from config import ADMINS

ts = URLSafeTimedSerializer(app.config["SECRET_KEY"])

def send_email(email,subject,html):
    msg = Message(subject,sender=ADMINS[0],recipients=[email])
    msg.html = html
    msg.body = html
    
    with app.app_context():
        mail.send(msg)