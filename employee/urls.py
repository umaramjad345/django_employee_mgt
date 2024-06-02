from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path("home/", home),
    path("add-emp/", add_emp)
]
