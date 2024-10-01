from django import forms
from .models import *

class ContactForm(forms.ModelForm):
    class meta:
        model = Contact
        # fields = '__all__'
        fields = ['full_name', 'email', 'phone', 'message']