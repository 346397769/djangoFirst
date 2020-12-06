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
]