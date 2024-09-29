from django.urls import path
from .views import *
urlpatterns = [
    path('', Home, name="home"),
    path('category', Contact, name="category"),
    path('blog', Contact, name="blog"),
    path("contact", index, name="contact"),
    path("about", about, name="about"),
    path("singleblog/<int:pk>", single_blog, name="singleblog"),
]
