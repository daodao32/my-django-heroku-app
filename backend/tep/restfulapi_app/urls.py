from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from .views import *

from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'', PostViewset, basename='list')
urlpatterns = router.urls