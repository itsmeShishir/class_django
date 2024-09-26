from django.contrib import admin
from .models import Contact


# Register your models here.
class ContactDetails(admin.ModelAdmin):
    list_display = ['email', 'full_name', 'phone']
    search_fields = ['email']
    # list_filter = ['']

admin.site.register(Contact, ContactDetails)