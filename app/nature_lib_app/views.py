from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from nature_lib_app.models import Post

class IndexView(ListView):
  template_name = 'nature_lib_app/index.html'
  model = Post

