from django.urls import path
from .views import *
urlpatterns = [
    path("", index, name="home" ),
    path("blog", home, name="blog" ),
    path("about", about, name="about" ),
    path("contact", contact, name="contact")
]
