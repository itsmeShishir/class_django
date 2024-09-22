from django.urls import path
from blog import views
from .views import *
urlpatterns = [
    path("blog", index, name="blog" ),
    path("", views.home, name="home" ),
]
