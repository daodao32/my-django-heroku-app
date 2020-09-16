from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from .views import *

app_name = 'restfulapi_app'
urlpatterns = [

    path('apihome/', RestfulApi.as_view(), name='apihome'),
    path('apilistview/', PostListView.as_view(), name='apilistview'),
    path('home/', ProjectHome.as_view(),name='home'),
]