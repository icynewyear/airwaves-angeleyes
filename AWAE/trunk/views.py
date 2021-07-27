from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import FormView, UpdateView, DeleteView

from .models import Trunk, EyeKey
# Create your views here.

class TrunkDetail(DetailView):
    model = Trunk
    template = "trunk/trunk_view.html"
    context_object_name = 'trunk'
