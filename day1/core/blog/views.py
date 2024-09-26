from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.

# 2 type of views-> 
# 1. function base views -> use decorator
# 2. class base views -> use metaclass

def Home(request):
    return HttpResponse("Hello from http Response home page")

#TODO
def Contact(request):
    redirect('home')



