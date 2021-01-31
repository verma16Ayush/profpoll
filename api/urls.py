from django.contrib import admin
from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.api_overview, name='api_overview'),
]