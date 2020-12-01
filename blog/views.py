from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView

def home(request):
    post_list = Post.objects.all().order_by("-date_posted")
    context = {
        "posts": post_list,

    }
    return render(request, "blog/home.html", context)

def post_list_view(request):
    post_list = Post.objects.all()
    context = {
        "posts": post_list,
    }
    return render(request, "blog/home.html", context) 


class PostListView(ListView):
    model = Post
    template_name = "blog/home.html" #looks for the view in this order <app>/<model>_<viewtype>.html
    context_object_name = "posts"
    ordering = ["-date_posted"]

class PostDetailView(DetailView):
    model = Post
    

def about(request):
    return render(request, "blog/about.html", {"title": "about"})





