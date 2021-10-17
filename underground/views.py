from django.contrib.admin.filters import ListFilter
from django.shortcuts import render
from django.views.generic import ListView, DeleteView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post
# Create your views here.

class BlogListView(ListView):
    model = Post
    template_name = 'home.html'

class BlogDetailView(DeleteView):
    model = Post
    template_name = 'post_detail.html'
class BlogCreateView(CreateView):
    model = Post
    template_name = 'new_post.html'
    fields = ['title', 'author','summary', 'body']
class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'edit_post.html'
    fields = ['title','summary', 'body']

class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')