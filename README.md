# Sample Flask Application

This application template is based on my learning of python from https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world
the best place to start with python web development. I am currently working on this application and implementing the concepts that are explained in this tutorial. <br>
So if you are interested in learning python web development then please follow this tutorial or join me and I will discribe all my understanding till now. And you can work with me on this project.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

## Prerequisites

What things you need to install the software and how to install them

### Windows Users:
### Install Python

Head to the python [homepage](https://www.python.org/) to download python.<br>
```
Download > Python <Version>
```
### Setup Environment Variable
We will be needing PIP(Python Package Installer) to download the required dependencies.
```
<localDirPath>\Programs\Python\Python37-32\Scripts  # Set this as system environment path.
```

### Setting Up Application

A step by step series of examples that tell you how to get a development env running

After successfully installing python and pip please verify the version of the python.
```
$ python --version
Python 3.7.0

$ pip --version
pip 18.1 from d:\experiments\python\sampleflaskapplication\venv\lib\site-packages\pip (python 3.7)
```
### Clone this repository
```
If you have not forked this repo.

$ git clone https://github.com/abhinav2127/SampleFlaskApplication.git

If you have forked this repo.

$ git clone https://github.com/<your_username>/SampleFlaskApplication.git
```

Before running this application we need to create virtual environment as we are working on dev environment.
```
$ pip install virtualenv    # to install virtual environment provider
$ pip install virtualenvwrapper-win # for Windows Users Only
$ virtualenv venv           # will create virtual environment for you.
$ venv\Scripts\activate     # this will activate your virtual environment.
(venv) ...>
```
Now you are all set.

We are working with Flask for creating this web application. So download the flask package.

```
(venv) $ pip install Flask
(venv) $ pip install Flask-wtf     # for installing Flask Webform.
(venv) $ setprojectdir .           # this will set the default project directory as the main directory
(venv) $ export FLASK_DEBUG=1      # enables debugging mode
(venv) $ flask run                 # to run your application.

* Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 305-291-976
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```
If you are seeing this message then your application is running successfully. <b>Hurray!</b>

Now click on http://127.0.0.1:5000/ link and open your application.

### Lets Setup your Database

We are working with SQLite database to store our records, and after that we will add mongoDb to store logs. In this way we can learn both databases.

The first is [Flask-SQLAlchemy](http://flask-sqlalchemy.pocoo.org/2.3/), an extension that provides a Flask-friendly wrapper to the popular [SQLAlchemy](https://www.sqlalchemy.org/) package, which is an [Object Relational Mapper](https://en.wikipedia.org/wiki/Object-relational_mapping) or ORM.

SQLAlchemy supports a long list of database engines, including the popular MySQL, PostgreSQL and SQLite.

To install Flask-SQLAlchemy in your virtual environment, make sure you have activated it first, and then run:

```
(venv) $ pip install flask-sqlalchemy
```

The second extension that I'm going to present in this chapter is [Flask-Migrate](https://github.com/miguelgrinberg/flask-migrate), which is actually one created by yours truly.

The installation process for Flask-Migrate is similar to other extensions you have seen:

```
(venv) $ pip install flask-migrate
```
### Create the Migration Repository

Flask-Migrate exposes its commands through the <b>flask</b> command. You have already seen <b>flask run</b>, which is a sub-command that is native to Flask. The <b>flask db</b> sub-command is added by Flask-Migrate to manage everything related to database migrations. So let's create the migration repository for microblog by running <b>flask db init</b>:
```
(venv) $ flask db init
  Creating directory /home/miguel/microblog/migrations ... done
  Creating directory /home/miguel/microblog/migrations/versions ... done
  Generating /home/miguel/microblog/migrations/alembic.ini ... done
  Generating /home/miguel/microblog/migrations/env.py ... done
  Generating /home/miguel/microblog/migrations/README ... done
  Generating /home/miguel/microblog/migrations/script.py.mako ... done
  Please edit configuration/connection/logging settings in
  '/home/miguel/microblog/migrations/alembic.ini' before proceeding.
```
### Lets migrate our tables
Now we will migrate the database and create the user table.
```
(venv) $ flask db migrate -m "Migrating database"
INFO  [alembic.runtime.migration] Context impl SQLiteImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
INFO  [alembic.autogenerate.compare] Detected added table 'user'
INFO  [alembic.autogenerate.compare] Detected added index 'ix_user_email' on '['email']'
INFO  [alembic.autogenerate.compare] Detected added index 'ix_user_username' on '['username']'
  Generating /home/miguel/microblog/migrations/versions/e517276bb1c2_users_table.py ... done
```

### Lets Upgrade Database
You will find that it has two functions called <b><i>upgrade()</i></b> and <b><i>downgrade()</b></i>. The <b><i>upgrade()</b></i> function applies the migration, and the </b></i>downgrade()</b></i> function removes it. This allows Alembic to migrate the database to any point in the history, even to older versions, by using the downgrade path.
```
(venv) $ flask db upgrade
INFO  [alembic.runtime.migration] Context impl SQLiteImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
INFO  [alembic.runtime.migration] Running upgrade  -> e517276bb1c2, users table
```

<b><i>downgrade()</i></b> is very helpful when you have issue with the migration query to downgrade the migration to the stable version.
### Test your database
Once in the Python prompt, let's import the database instance and the models:
```
>>> from app import db
>>> from app.models import User, Post
```
Start by creating a new user:
```
>>> u = User(username='john', email='john@example.com')
>>> db.session.add(u)
>>> db.session.commit()
```
Let's add another user:
```
>>> u = User(username='susan', email='susan@example.com')
>>> db.session.add(u)
>>> db.session.commit()
```
The database can answer a query that returns all the users:
```
>>> users = User.query.all()
>>> users
[<User john>, <User susan>]
>>> for u in users:
...     print(u.id, u.username)
...
1 john
2 susan
```
Here is another way to do queries. If you know the id of a user, you can retrieve that user as follows:
```
>>> u = User.query.get(1)
>>> u
<User john>
```
Now let's add a blog post:
```
>>> u = User.query.get(1)
>>> p = Post(body='my first post!', author=u)
>>> db.session.add(p)
>>> db.session.commit()
```
To complete this session, let's look at a few more database queries:
```
>>> # get all posts written by a user
>>> u = User.query.get(1)
>>> u
<User john>
>>> posts = u.posts.all()
>>> posts
[<Post my first post!>]

>>> # same, but with a user that has no posts
>>> u = User.query.get(2)
>>> u
<User susan>
>>> u.posts.all()
[]

>>> # print post author and body for all posts 
>>> posts = Post.query.all()
>>> for p in posts:
...     print(p.id, p.author.username, p.body)
...
1 john my first post!

# get all users in reverse alphabetical order
>>> User.query.order_by(User.username.desc()).all()
[<User susan>, <User john>]
```
The [Flask-SQLAlchemy](http://flask-sqlalchemy.pocoo.org/2.3/) documentation is the best place to learn about the many options that are available to query the database.<br>
To complete this section, let's erase the test users and posts created above, so that the database is clean and ready for the next chapter:
```
>>> users = User.query.all()
>>> for u in users:
...     db.session.delete(u)
...
>>> posts = Post.query.all()
>>> for p in posts:
...     db.session.delete(p)
...
>>> db.session.commit()
```
### Learn Password Hashing
The following Python shell session demonstrates how to hash a password:
```
>>> from werkzeug.security import generate_password_hash
>>> hash = generate_password_hash('foobar')
>>> hash
'pbkdf2:sha256:50000$vT9fkZM8$04dfa35c6476acf7e788a1b5b3c35e217c78dc04539d295f011f01f18cd2175f'
```

The verification process is done with a second function from Werkzeug, as follows:

```
>>> from werkzeug.security import check_password_hash
>>> check_password_hash(hash, 'foobar')
True
>>> check_password_hash(hash, 'barfoo')
False
```
<i> **Note:** The whole password hashing logic can be implemented as two new methods in the user model: Path: app/model.py</i>

Here is an example usage of these new methods:
```
>>> u = User(username='susan', email='susan@example.com')
>>> u.set_password('mypassword')
>>> u.check_password('anotherpassword')
False
>>> u.check_password('mypassword')
True
```
## Lets Setup Project Dependency

### Flask-Login
In this chapter I'm going to introduce you to a very popular Flask extension called [Flask-Login](https://flask-login.readthedocs.io/en/latest/)

To be ready for this chapter, you can start by installing Flask-Login in your virtual environment:
```
(venv) $ pip install flask-login
```
*As with other extensions, Flask-Login needs to be created and initialized right after the application instance in app/___init___.py.*

Now as a step forward to setup user model please review the usermodel.

### Setup Mailing credential on your environment
I have used mailing server to send error logs on your email if you don't want this feature you need not set the configurations. This feature is helpful if you are using this application for production server since error stack trace can only be seen on the console.

Here are the configurations that we need to take care:

- MAIL_SERVER: smtp.gmail.com (For GMail)
- MAIL_PORT: 465 (SSL port for GMail)
- MAIL_USE_TLS: yes/no (it is optional)
- MAIL_USERNAME: Your full Gmail address (e.g. yourusername@gmail.com)
- MAIL_PASSWORD: Your Gmail password

After Setting up the configurations for mailing server I would suggest you to add your application administrators mail ids in the **ADMINS** array *ADMINS = ['your-email@example.com']*
```
export MAIL_SERVER=smtp.googlemail.com
export MAIL_PORT=465
export MAIL_USE_TLS=1
export MAIL_USERNAME=<your-gmail-username>
export MAIL_PASSWORD=<your-gmail-password>
```

## Built With

* [Python](https://docs.python.org/3/) - Open source programming language
* [Flask](http://flask.pocoo.org/docs/1.0/) - Framework for Web application development

## Features
- User and User Profile
  - User Login and Registration
  - Last Visiting Time for User
- Web Forms
- SQL Light Database
- Profile Picture (Using Avatars)
- Error Handling
  - Custom Error Pages
  - Email error Messages
  - Logging to a file
- Followers and Followers Posts

## Contributing

Please read CONTRIBUTING.md for details on our code of conduct, and the process for submitting pull requests to us.

## Authors

* **Abhinav Jha** - *Initial work* - [ProjectOnion](https://github.com/abhinav2127/ProjectOnion)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Thankful for Miguel Grinberg.
