============================
PyCon TW website
============================

This repository stores the PyCon TW website, forked from PyCon US website developed by Eldarion. This
project is open source and the license can be found in LICENSE.


Installation
============

To get setup with pycon code you must have the follow installed:

 * Python 2.5+
 * virtualenv 1.4.7+
 * C compiler (for PIL)

Setting up environment
----------------------

Create a virtual environment where pycon dependencies will live::

    $ virtualenv --no-site-packages pycon
    $ source pycon/bin/activate
    (pycon)$

Install pycon project dependencies::

    (pycon)$ pip install -r requirements.txt


Setting up the database
-----------------------

This will vary for production and development. By default the project is set
up to run on a SQLite database. If you are setting up a production database
see the Configuration section below for where to place settings and get the
database running. Now you can run::

    (pycon)$ python pycon_project/manage.py syncdb
    (pycon)$ python pycon_project/manage.py loaddata fixtures/initial_{wakawaka,boxes}.json

The wakawaka fixtures will require a user to exist before being ran. During
syncdb it is worth it to make a superuser account which can then be used for
making other users staff/superusers after they sign up.

Running a web server
--------------------

In development you should run::

    (pycon)$ python pycon_project/manage.py runserver
