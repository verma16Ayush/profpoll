Project ProfPoll
================

    **NOTE:** This project was made as a submission prototype for
    SPEC-NITH's national hackathon ELECTROTHON-3.0. This is just the
    backend part of the project, still under development. To visit the
    frontend of the project by @rv60231023 visit his
    `repo <https://github.com/rv299792458/profpoll_front>`__.

This project aims at providing an anonymous yet, authenticated platform
for students of NITH to rate and review their professors free of any
undue repurcussions that may be levied if they were to speak out in the
open. Thus, the main aim of the project is to provide a platform for
unbiased and unadulterated constructive reviews about professors and, in
future, various other aspects of the college across the spectrum ranging
from administration, accomodation etc.

Project Tree
------------

::

        profpoll
        ├─ .gitignore
        ├─ README.md
        ├─ README2.md
        ├─ api
        │  ├─ __init__.py
        │  ├─ admin.py
        │  ├─ apps.py
        │  ├─ migrations
        │  │  ├─
        │  ├─ models.py
        │  ├─ serializers.py
        │  ├─ tests.py
        │  ├─ urls.py
        │  ├─ views.py
        │  └─ webscraper.py
        ├─ manage.py
        ├─ profpoll
        │  ├─ __init__.py
        │  ├─ asgi.py
        │  ├─ settings.py
        │  ├─ urls.py
        │  └─ wsgi.py
        └─ requirements.txt

How to get Started With the Project?
------------------------------------

    NOTE: if you want to just modify the project for personal use, you
    can go right ahead and clone it. However, if you aim at
    collaborating and making PRs, it is recommended that you first fork
    your own copy of the project and then clone.

This documentation is oriented to setting up the project in vscode using
a virtual enviornment.

Clone the project:

.. code:: bash

        git clone https://www.github.com/verma16Ayush/profpoll.git

cd into the project directory:

.. code:: bash

        cd profpoll

create a virtual enviornment and activate it, This document uses
``python3``'s venv tool. Feel free to use any other that you like.

.. code:: bash

        python3 -m venv .venv
        ./.venv/bin/activate

First we will need to install dependencies. All the dependencies are
neatly frozen using ``pip freeze`` into the ``requirements.txt`` file.
In case any new dependencies are installed, make sure to add them to
requirements.txt file To install the dependencies:

.. code:: bash

        pip install -r requirements.txt

    To list any new dependencies that were installed

.. code:: bash

        pip freeze > requirements.txt

migrate the database changes.

.. code:: bash

        python manage.py makemigrations
        python manage.py migrate

Once all the migrations are setup, a superuser must be created to
acquire administrative privileges.

.. code:: bash

        python manage.py createsuperuser

and follow prompted instructions.

Once all the above steps are completed successfully, the project is
ready to be served over a localhost. To do that:

.. code:: bash

        python manage.py runserver

The djnago-admin panel must now be accessible. Simply go the your
browser and type into the address bar:

::

    http://127.0.0.1:8000/admin/

where ``127.0.0.1:8000`` should be replaced with with the LAN's IP if
the project is being over it as described in the ``OPTIONAL`` section.
This should be followed all through the rest of this ``README.md`` file.

The API
-------

The project implements a REST API that could later be consumed by a
frontend built over any desired tech stack. Therefore, all ``GET``
requests return a ``JSON`` response whereas all ``POST`` requests should
be made with an appropriate ``JSON`` object as well.

Overview
^^^^^^^^

To get an overview of all available API endpoints, go to:

::

    http://127.0.0.1:8000/api/

this would return a json response that will look like:

.. code:: json

        {
            "api/":"api end-points overview",
            "api/list/":"list all professors in database",
            "api/list_dept/<str:dept>/":"list all professors of 'dept' department",
            "rate_prof/<str:pk>/":"rate professor with 'pk' primary key",
            "prof_id/<str:pk>/":"get a professor's data, including ratings but not 
            comments with 'pk' primary key",
            "prof_comment_id/<str:pk>/":"get comments on a professor with 'pk' 
            primary key",
            "review/<str:pk>/":"write a review/comment for a professor with 'pk' 
            primary key",
            "register/":"register a new user",
            "login_user/":"login an existing user",
            "logout_user/":"log out an already logged-in user"
        }

this list signifies all the available endpoints we can make requests to.

Contributions/Collaborations
----------------------------

Contribution are always welcome however if you want to collaborate on
the project with me, it would be preferable if you are a student of
NITH. feel free to mail me at verma16.ayush@gmail.com
