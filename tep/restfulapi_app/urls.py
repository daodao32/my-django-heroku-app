from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from .views import *

urlpatterns = [
    path('apihome/', RestfulApi.as_view()),
      path('home/', ProjectHome.as_view()),
]