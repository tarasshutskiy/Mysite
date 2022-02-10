from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *

# Create your views here.
class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'

class PostDetailView(DetailView):
    model = Post
    slug_field = 'slug'
    template_name = 'post_detail.html'



