from django.db import models

# Create your models here.
class Contact(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.IntegerField()
    message = models.TextField()

    def __str__(self):
        return f"{self.email}"