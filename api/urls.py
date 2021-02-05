from django.contrib import admin
from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.api_overview, name='api_overview'),
    path('list/', views.get_prof_list, name='get_prof_list'),
    path('list_dept/<str:dept>/', views.get_prof_list_by_dept, name='list_by_dept'),
    path('rate_prof/<str:pk>/', views.rate_prof, name='rate_prof'),
    path('prof_id/<str:pk>/', views.get_prof_id, name='get_prof_id'),
    path('prof_comment_id/<str:pk>/', views.get_prof_comments, name='get_prof_comments'),
    path('review/<str:pk>/', views.review_prof, name='review_prof'),
    path('register/', views.register, name='register'),
    path('login_user/',views.login_user, name='login_user'),
    path('logout_user/', views.logout_user, name='logout_ser'),
]