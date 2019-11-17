
from django.contrib import admin
from django.urls import path

from FrenchVo import views

urlpatterns = [
    path('', views.index),
    path('phrase', views.phrase),
]
