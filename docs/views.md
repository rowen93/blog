# views
from django.http import HttpResponse

## passing content into the view.

def post_list_view(request):
    context = {
        "posts": Post.objects.all()
    }
    return render(request, "blog/home.html", context) 