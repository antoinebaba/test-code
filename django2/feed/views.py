#from django.shortcuts import render
from django.views.generic import ListView
from .models import Post
from django.db.models.query import QuerySet
from django.views.generic import ListView, DetailView

# Create your views here.

class HomePage(ListView):
    http_method_names= ["get"]
    template_name = "feed/homepage.html"
    model = Post
    context_object_name = "posts"
    QuerySet = Post.objects.all().order_by('-id')[0:30]

class PostDetailView(DetailView):
    http_method_names = ["get"]
    template_name = "feed/detail.html"
    model = Post
    context_object_name = "post{{ post }}"