from django.urls import path
from .views import *

urlpatterns = [
   path('contactus', FormContact, name="contact-us"),
   path('listcontact', listContact, name="contact-list"),
   path('messagesuccess', messageSuccess, name="success"),
   path('messageerror', messageError, name="error"),
   path('admincontact', AdminContact, name="admincontact"),
   path('deletecontact/<int:id>', DeleteContact, name="deletecontact"),
   path('updatecontact/<int:id>', UpdateContact, name="updatecontact"),
]
