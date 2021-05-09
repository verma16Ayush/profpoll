.. profpoll documentation master file, created by
   sphinx-quickstart on Sun May  9 16:52:48 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Project profpoll
================

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

.. toctree::
   :maxdepth: 2

   HowTo/how_to.rst
   Reference/reference.rst
   Tutorials/tutorials.rst
   Explanations/explanations.rst
