from django.shortcuts import render
from .models import *
from django.views.generic import FormView,TemplateView,CreateView,ListView,UpdateView,DetailView
from datatableview.views import XEditableDatatableView, DatatableView


class ProjectHome(TemplateView):
    template_name='home/project_home.html'
