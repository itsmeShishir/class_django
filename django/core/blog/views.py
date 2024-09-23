from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog
# Create your views here.
def index(request):
    blog = Blog.objects.all()
    return render(request, "index.html", {blog: "blog"})
def home(request):
    return render(request, "blog.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")
