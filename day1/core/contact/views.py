from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
# Create your views here.
from .forms import ContactForm
from django.contrib.auth.decorators import login_required

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

@login_required
def AdminContact(request):
    contact = Contact.objects.all()
    return render(request, "admin/allcontact.html", {"contact": contact})

@login_required
def DeleteContact(request,id):
    contact = get_object_or_404(Contact, id=id)
    if request.method == "POST":
        contact.delete()
        return redirect("admincontact")
    return render(request, "admin/deletecontact.html")
@login_required
def UpdateContact(request, id):
    contact = get_object_or_404(Contact, id=id)
    if request.method == "POST":
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:   
        form = ContactForm(instance=contact)

    context = {
        "form": form
    }
    
    return render(request, "admin/updateContact.html", context)
        