from django.shortcuts import render
from .models import *
from django.views.generic import FormView,TemplateView,CreateView,ListView,UpdateView,DetailView
from datatableview.views import XEditableDatatableView, DatatableView
from datatableview import helpers, Datatable, columns
import csv
from django.http import HttpResponse, JsonResponse
from django.views.generic.edit import CreateView, DeleteView, UpdateView,View
from django import template
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.core import serializers
import json
from django.core.serializers.json import DjangoJSONEncoder
from datetime import datetime, timedelta, timezone

from rest_framework.response import Response
from rest_framework.views import APIView

class RestfulApi(APIView):

    def get(self,request,*args,**kwargs):
        data={'a':'apple','b':'banana'}

        return Response(data)
