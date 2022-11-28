from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('may/', views.may, name='may'),
    path('june/', views.june, name='june'),
    path('july', views.july, name='july'),
    path('november', views.november, name='november'),
]
