from django.shortcuts import render
from .models import Post
# from django.http import HttpResponse


def home(request):
    # return HttpResponse("<h1>Blog home!</h1>")
    context = {
        "posts": Post.objects.all()
    }
    return render(request, "blog/home.html", context)


def about(request):
    # return HttpResponse("<h1>About Page</h1>")
    return render(request, "blog/about.html", {"title": "About"})
