from django.shortcuts import render, redirect
from .models import *
from .forms import *
# Create your views here.

from django.shortcuts import render, redirect
from .forms import ContactForm

def FormContact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:   
        form = ContactForm()

    context = {
        "form": form
    }
    
    return render(request, "user/contact.html", context)


def listContact(request):
    return render(request, "user/listcontact.html")

def messageSuccess(request):
    return render(request, "message/success.html")

def messageError(request):
    return render(request, "message/error.html")

def AdminContact(request):
    contact = Contact.objects.all()
    return render(request, "admin/allcontact.html", {"contact": contact})

def DeleteContact(request, pk):
     if request.method == "POST":
         contact = Contact.objects.get(id=pk)
         contact.delete()
         return redirect("admincontact")
     else:
         pass
    
        