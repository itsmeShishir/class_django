from django import forms
from .models import BlogCategory

# class CategoryForm(forms.ModelForm):
#     class Meta:
#         model = BlogCategory
#         fields = '__all__'
    

class CategoryForm(forms.Form):
    category_name = forms.CharField(max_length=255)
    category_img = forms.ImageField(required= False, allow_empty_file=True)