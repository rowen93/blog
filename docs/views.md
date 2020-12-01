# views
from django.http import HttpResponse

## passing content into the view.

def post_list_view(request):
    context = {
        "posts": Post.objects.all()
    }
    return render(request, "blog/home.html", context) 

## class based views 
types..
list views, detail views, create views, update, views, delete views

#looks for the view in this order <app>/<model>_<viewtype>.html