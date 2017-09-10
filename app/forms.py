from flask_wtf import Form
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired,EqualTo,ValidationError
from . import db, models



class signUpForm(Form):
    username = StringField('Username',validators=[DataRequired()])
    email = StringField('Email',validators=[DataRequired(),EqualTo('vEmail', message='Emails dont match')])
    vEmail = StringField('vEmail',validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(),EqualTo('vPassword', message='Passwords dont match')])
    vPassword = PasswordField('vPassword', validators=[DataRequired()])
    accept_tos = BooleanField('I accept the TOS', validators=[DataRequired()])
    
    def validate_username(form,field):
        users = models.User.query.filter_by(userName=field.data.lower()).all()
        if len(users):
            raise ValidationError('this user name is taken')
    
    def validate_email(form,field):
        users = models.User.query.filter_by(email=field.data).all()
        if len(users):
            raise ValidationError('This email is taken you should try to recover your passord instead')
    
    def validate_accept_tos(form,field):
        if field.data != True:
            raise ValidationError('You must accept the terms of service')
            
class LoginForm(Form):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('remember_me')
    
    def validate_password(form,field):
        user = form.username.data.lower()
        pw = field.data
        user = models.User.query.filter_by(userName=user).first()
        if not user or not user.testPassword(pw):
            raise ValidationError('Your Username Passwords Do  Not Match')
        
        if not user.emailVerified:
            raise ValidationError('you need to verify you email before you can Sign In')
