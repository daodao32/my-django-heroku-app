from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from .views import *


app_name = 'home'
urlpatterns = [
    path('home/', ProjectHome.as_view(),name='home'),
]

