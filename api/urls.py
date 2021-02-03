from django.contrib import admin
from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.api_overview, name='api_overview'),
    path('prof_list/', views.prof_list, name='prof_list'),
    path('prof_by_dept/<str:dept>/', views.profs_by_dept, name='prof_by_dept'),
    path('prof_rating/<str:pk>/', views.prof_rating, name='prof_rating'),
    path('prof_comments/,str:pk>', views.prof_comments, name='prof_comments'),
]