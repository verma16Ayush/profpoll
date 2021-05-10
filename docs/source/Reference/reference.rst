.. _reference:

.. role:: raw-html(raw)  

:format: html

=============
API Reference
=============

The Project is still under development. API Reference, as of now, is
intended only for testing and debugging processes.

``GET`` ``api/``  Permissions: ``AllowAny``
++++++++++++++++++++++++++++++++++++++++++++++++
Retruns an overview of all available api endpoints.

``GET`` ``api/list/`` Permissions: ``IsAuthenticatedOrReadOnly``
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Returns a json response of all professors

``GET`` ``api/list_dept/<str:dept>/`` Permissions: ``IsAuthenticatedOrReadOnly``
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Returns a json response of all professors of a given department denoted by 
``dept`` argument in the URL.

``GET`` ``api/prof_id/<str:pk>/`` Permissions: ``IsAuthenticatedOrReadOnly``
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Get data on a professor with pk primary key. The returned json response does
not contain comment reviews of the said professor.

``GET`` ``api/prof_comment_id/<str:pk>/``  Permissions: ``IsAuthenticatedOrReadOnly``
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Get comment reviews on a professor with pk primary key.

``POST`` ``api/rate_prof/<str:pk>/`` Permissions: ``IsAuthenticated`` 
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Post a json request to rate a professor with given pk primary key

``POST`` ``api/review/<str:pk>/`` Permissions: ``IsAuthenticated``
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Post a json request to comment review a professor. Available only
to authenticated instances.

``POST`` ``api/register/`` Permissions: ``AllowAny``
++++++++++++++++++++++++++++++++++++++++++++++++++++
Post a json request to register a new user

``POST`` ``api/login_user/`` Permissions: ``AllowAny``
++++++++++++++++++++++++++++++++++++++++++++++++++++++
Post a json request to login a pre-existing user

``POST`` ``api/logout_user`` Permissions: ``IsAuthenticated``
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Post a json request to logout an already logged-in user.