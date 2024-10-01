from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Blog, BlogCategory
# Create your views here.
# 2 type of views-> 
# 1. function base views -> use decorator
# 2. class base views -> use metaclass

def Home(request):
    blog = Blog.objects.all()
    category = BlogCategory.objects.all()
    context = {
        "category": category,
        "blog": blog
    }
    return render(request, "user/index.html", context)

def index(request):
    context = {
        "name":"shishir"
    }
    return render(request, "user/index.html", context)

def about(request):
    return render(request, "user/about.html")

def single_blog(request, pk):
    blog = Blog.objects.get(id=pk)
    print(blog)
    context = {
        "blog": blog
    }
    return render(request, "user/singleblog.html", context)