from django.contrib import admin
from .models import *
# Register your models here.
class BlogDetailsCategory(admin.ModelAdmin):
    list_display = ['category_name', 'created_at']
    search_fields = ['category_name']

class BlogDetails(admin.ModelAdmin):
    list_display = ['title', 'description', 'category', 'created_at']
    search_fields = ['title']
    list_filter = ['created_at']

admin.site.register(BlogCategory, BlogDetailsCategory)
admin.site.register(Blog, BlogDetails)


