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
from rest_framework.generics import ListAPIView

from .serializers import PostSerializer
from .models import *
class RestfulApi(APIView):
    # tempalte_name = 'restfulapi_app/apihome.html'
    def get(self,request,*args,**kwargs):
        sq=Post.objects.all()
        serializer = PostSerializer(sq,many=True) 
        return Response(serializer.data)
        

    def post(self,request,*args,**kwargs):
        serializer = PostSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class PostListView(ListAPIView):
    queryset= Post.objects.all()
    serializer_class = PostSerializer


class ProjectHome(TemplateView):
    template_name='restfulapi_app/project_home.html'
