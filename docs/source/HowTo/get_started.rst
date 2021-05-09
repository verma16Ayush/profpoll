.. _get-started:

Get Started in a virtual enviornment
====================================

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
