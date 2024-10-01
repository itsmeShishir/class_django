from django import forms

class ContactForm(forms.Form):
    category_name = forms.CharField(max_length=255)
    category_img = forms.ImageField(upload_to="category/", null=True, blank=True)
    