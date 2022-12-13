from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('test2/', views.test2 , name='test2'),
    path('newEvent/', views.newEvent, name='newEvent'),
    path('timeline/', views.timeline, name='timeline'),
    path('spatialdata/', views.spatialdata, name='spatialdata')
]
