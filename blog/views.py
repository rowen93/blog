from django.shortcuts import render

from .models import Post

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
    
def about(request):
    return render(request, "blog/about.html", {"title": "about"})




