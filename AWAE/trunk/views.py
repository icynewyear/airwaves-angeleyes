from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import FormView, UpdateView, DeleteView
from django.http import JsonResponse

from .models import Trunk, EyeKey
# Create your views here.

class TrunkDetail(DetailView):
    model = Trunk
    template = "trunk/trunk_view.html"
    context_object_name = 'trunk'


def seed_word(request):
    if request.is_ajax and request.method == "GET":
        word = request.GET.get("word", None)
        if word == "eye":
            
            print("eye")
        data = {}
    return JsonResponse(data)
