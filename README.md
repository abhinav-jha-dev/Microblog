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
$ pip install Flask
$ pip install Flask-wtf     # for installing Flask Webform.
$ setprojectdir .           # this will set the default project directory as the main directory
$ flask run                 # to run your application.

* Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```
If you are seeing this message then your application is running sucessfully. <b>Hurray!</b>

Now click on http://127.0.0.1:5000/ link and open your application.

### Setting Up Database

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

Now we will migrate the database and create the user table.
```
(venv) $ flask db migrate -m "users table"
INFO  [alembic.runtime.migration] Context impl SQLiteImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
INFO  [alembic.autogenerate.compare] Detected added table 'user'
INFO  [alembic.autogenerate.compare] Detected added index 'ix_user_email' on '['email']'
INFO  [alembic.autogenerate.compare] Detected added index 'ix_user_username' on '['username']'
  Generating /home/miguel/microblog/migrations/versions/e517276bb1c2_users_table.py ... done
```
You will find that it has two functions called <b><i>upgrade()</i></b> and <b><i>downgrade()</b></i>. The <b><i>upgrade()</b></i> function applies the migration, and the </b></i>downgrade()</b></i> function removes it. This allows Alembic to migrate the database to any point in the history, even to older versions, by using the downgrade path.
```
(venv) $ flask db upgrade
INFO  [alembic.runtime.migration] Context impl SQLiteImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
INFO  [alembic.runtime.migration] Running upgrade  -> e517276bb1c2, users table
```

## Built With

* [Python](https://docs.python.org/3/) - Open source programming language
* [Flask](http://flask.pocoo.org/docs/1.0/) - Framework for Web application development

## Contributing

Please read CONTRIBUTING.md for details on our code of conduct, and the process for submitting pull requests to us.

## Authors

* **Abhinav Jha** - *Initial work* - [ProjectOnion](https://github.com/abhinav2127/ProjectOnion)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Thankful for Timmy Reill's blog.
