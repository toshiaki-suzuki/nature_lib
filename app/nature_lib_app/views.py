from django.shortcuts import render
from django.views.generic import TemplateView

class IndexView(TemplateView):
  template_name = 'nature_lib_app/index.html'
