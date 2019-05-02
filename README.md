# Django Blog Mini-Project

A simple blog app written with Django.

## Initial Steps

1. Setting up a virtual environment
    1. check python versions `python -V` and `python3 -V`. If two versions of python are present do the following:
        1. create a new directory `mkdir DjangoFirst` and `cd DjangoFirst` into it
        1. create a virtual environment `virtualenv -p python3 .` (if no python, just python3 you can just do `virtualenv .` instead) If it does not exist run `sudo pip3 install virtualenv` to install it globally
        1. Activate virtual environment `source bin/activate`
        1. TO deactivate run `deactivate`
1. Installing Django `sudo pip3 install django==1.11` or `sudo pip3 install Django` to install new
1. To check installed version `python3 -m django --version`
1. Saving requirements file `sudo pip3 freeze --local > requirements.txt`
1. List all available applications with `django-admin`
1. Creating a project in current directory `django-admin startproject mysite`
1. Or, Creating a project in the root directory `django-admin startproject mysite .`
7. Run `python3 manage.py runserver` to start Django development server

    Directory tree

    - root directory
        - manage.py
        - blog
            - __init__.py
            - settings.py
            - urls.py
            - wsgi.py

    **manage.py** allows us to run command line commands
    **__init.py__** it tells Python that this is Python package
    **settings.py** this is where we will change different settings and configurations including SECRET_KEY, DEBUG, INSTALLED_APPS section and more
    **urls.py** this is where we will set up a mapping from certain URLs to where we sent the user
    **wsgi.py** this is how our Python web application and the web server communicate

    127.0.0.1 = local host

8. Initialize Git `git init`
9. Hide certain files inside .gitignore `echo -e "*.sqlite3\n*.pyc\n__pycache__/" > .gitignore`
10. Add files and commit changes
11. Sync [travis](travis-ci.org) with git repository by clicking on `build unknown` and copy text for markdown and paste into README file
12. create new file to integrate with travis called `.travis.yml`

[![Build Status](https://travis-ci.com/danielsky81/django_blog_app.svg?branch=master)](https://travis-ci.com/danielsky81/django_blog_app)