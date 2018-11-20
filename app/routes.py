from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user={'username':'miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home',user=user, posts=posts)

'''
The first new thing in this version is the methods argument in the route decorator. 
This tells Flask that this view function accepts GET and POST requests,
overriding the default, which is to accept only GET requests.
The HTTP protocol states that GET requests are those that return information to the
client (the web browser in this case). All the requests in the application so far are
of this type. POST requests are typically used when the browser submits form data to the
server (in reality GET requests can also be used for this purpose, but it is not a recommended practice). 

The flash() function is a useful way to show a message to the user. A lot of applications
use this technique to let the user know if some action has been successful or not.
'''
    
@app.route('/login', methods=['GET', 'POST'])
def login():
    form= LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html',title='Sign In', form=form)