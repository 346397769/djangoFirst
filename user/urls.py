from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'user'
urlpatterns = [
    path('register', views.register, name="register"),
    path('login', views.login, name="login"),
    path('show', views.show, name="show"),
    path('delete', views.delete, name="delete"),
    path('update', views.update, name="update"),
    path('user_login', views.user_login, name="user_login"),
    path('user_register', views.user_register, name="user_register"),
    path('logout', views.logout, name="logout"),
    path('is_login', views.is_login, name="is_login"),
]
