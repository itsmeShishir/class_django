from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the blog index.")
def home(request):
    return HttpResponse("Hello, my name is shsihir.")

def about(request):
    return render(request, "index.html")
