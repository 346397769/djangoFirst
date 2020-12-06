from django.urls import path

from . import views

urlpatterns = [
    path('input/', views.input, name="input"),
    path('infoSubmit/', views.dealSubmit),
    path('download/', views.download, name="download"),
]