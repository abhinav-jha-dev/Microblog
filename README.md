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
