from django.urls import path
from .views import *
urlpatterns = [
    path('', Home, name="home"),
    path("about", about, name="about"),
    path("singleblog/<int:pk>", single_blog, name="singleblog"),
    path('addcategory', AddCategory, name="addcategory")
]
