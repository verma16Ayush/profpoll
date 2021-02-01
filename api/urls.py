from django.contrib import admin
from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.api_overview, name='api_overview'),
    path('profs/', views.prof_list, name='prof_list'),
    path('get_prof/', views.get_prof, name='get_prof'),
    path('prof_comment/<str:pk>/', views.prof_comment, name='prof_comment'),
    path('post_comment/<str:pk>/', views.post_comment, name='post_comment'),
    path('edit_comment/<str:pk>/', views.edit_comment, name='edit_comment'),
    path('delete_comment<str:pk>/', views.delete_comment, name='delete_comment'),
    path('upvote_comment/<str:pk/', views.upvote_comment, name='upvote_comment'),
]