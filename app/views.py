from flask import redirect, render_template, url_for, g,session,request
from flask_login import login_user, logout_user, current_user, login_required

from . import app,db, models,lm
from .forms import signUpForm, LoginForm
from .util import ts, send_email


@app.before_request
def before_request():
    g.user = current_user

@lm.user_loader
def load_user(id):
    return models.User.query.get(int(id))

@app.route('/')
@app.route('/index')
@login_required
def index():
    user = g.user
    user = {'nickname': 'some user name'}  # fake user
    return render_template('index.html',
                           title='Home',
                           user=user)
                           
@app.route('/login', methods=['GET', 'POST'])
def login():
    if g.user and g.user.is_authenticated:return redirect(url_for('index'))
    
    form = LoginForm()
    
    if form.validate_on_submit():
        user = models.User.query.filter_by(userName=form.username.data.lower()).first()
        login_user(user, remember = form.remember_me.data)
        return redirect(request.args.get('next') or url_for('index'))
    
    return render_template('login.html',
                           title='Sign In',
                           form=form)
    
@app.route('/signup', methods=["GET", "POST"])
def signup():
    form = signUpForm()
    if form.validate_on_submit():
        user = models.User(userName=form.username.data.lower(), 
                           password=form.password.data,
                           email=form.email.data)
        db.session.add(user)
        db.session.commit()
        
        # Now we'll send the email confirmation link
        subject = "Confirm your email"
        
        token = ts.dumps(user.email, salt='email-confirm-key899')
        
        confirm_url = url_for(
            'confirm_email',
            token=token,
            _external=True)
        
        html = render_template('activate.html',confirm_url=confirm_url)
        send_email(user.email, subject, html)
        return redirect(url_for('index'))
    
    return render_template('signup.html', form=form)

@app.route('/confirm/<token>')
def confirm_email(token):
    try:
        email = ts.loads(token, salt='email-confirm-key899')#, max_age=86400)
    except:
        abort(404)

    user = models.User.query.filter_by(email=email).first()
    if not user:abort(404)

    user.emailVerified = True

    db.session.add(user)
    db.session.commit()

    return redirect(url_for('login'))

@app.route('/signout')
def signout():
    logout_user()

    return redirect(url_for('index'))