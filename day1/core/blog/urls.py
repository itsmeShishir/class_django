from django.urls import path
from .views import *
urlpatterns = [
    path('', Home, name="home"),
    path('myname', Contact, name="contact"),
    path("home", index, name="index"),
    path("about", about, name="about"),
]
