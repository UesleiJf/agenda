# Description

This project aims to maintain an appointment schedule for tracking dates and payments.
It is designed for the Django RestFramework administrative area only, so we will not have any API or any external access for a possible query.

### Work environment details

* OS: Ubuntu 16.04 LTS
* IDE: PyCharm Community
* Terminal: Terminal
* Database: sqlite3

### Library Versions

* Python:   3.6
* Django:   2.2
* Babel: 2.6.0
* Django Rest Framework: 3.9.3
* dj-database-url: 0.5.0
* dj-static: 0.0.6
* python-dateutil: 2.8.0
* django-rest-swagger: 2.2.0

### Installation

First, you need to clone this project from Bitbucket:

git clone https://github.com/UesleiJf/agenda

This project run under Python 3.6 and Django 2.2

After clone, you need to install all the requirements. 

The Python >= 3.3 comes with venv to creating lightweight "virtual environments".

For this project, python3.6 was used

For full documentation for venv, you can see here:
https://docs.python.org/3/library/venv.html

To create an enviroment, run:

    python3.6 -m venv /path/to/new/virtual/environment

Run the command below to update the pip and avoid dependency conflicts when installing requirements.txt

    pip install --upgrade pip

Navigate to the directory /systemcall/ and execute the commands below

Now, you can install al the project requirements:

    pip install -r requirements.txt

After this, just execute the commands makemigrations and migrate to create project tables

    python3.6 manage.py makemigrations

    python3.6 manage.py migrate

    python3.6 manage.py collectstatic

## API

You now need to create a superuser to gain access to the administrative part of the system. (This will be the only developed area of the system)

    python3.6 manage.py createsuperuser

Now, you can start the project:

    python3.6 manage.py runserver

### To access the administrative area at the URL

    localhost:8000/admin


# Deploy to Heroku

### Creating the Git repository in the project root folder

    apt-get update
    
    apt-get install git-core
    
    git init
    
### Creating the app at Heroku

You should install heroku CLI tools in your computer previously (See http://bit.ly/2jCgJYW)

    heroku apps:create app-name (Remember to grab the address of the app in this point)

### Setting the allowed hosts

include your address at the ALLOWED_HOSTS directives in settings.py - 
Just the domain, make sure that you will take the protocol and slashes from the string

### Heroku install config plugin

Sending configs from .env to Heroku ( You have to be inside tha folther where .env files is)

    heroku plugins:install heroku-config
    heroku config:push -a

To show heroku configs do

    heroku config
    
### Publishing the app

    git add .
    git commit -m 'Configuring the app'
    git push heroku master --force
    
### Creating the data base

    heroku run python3.6 manage.py migrate
    
### Creating the Django admin user

    heroku run python3 manage.py createsuperuser
    
### Creating by UesleiJF
