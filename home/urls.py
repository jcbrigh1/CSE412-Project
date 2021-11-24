from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('searchName/', views.searchName),
    path('searchPerson/', views.searchPerson),
    path('searchGenreStyle/', views.searchGenreStyle),
]