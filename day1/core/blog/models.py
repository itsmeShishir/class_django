from django.db import models

# Create your models here.
class BlogCategory(models.Model):
    category_name = models.CharField(max_length=255)
    category_img = models.ImageField(upload_to="category/", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.category_name} and {self.created_at}"

class Blog(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE, null=True, blank=True)
    blog_img = models.ImageField(upload_to="blog/", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} and {self.category}"
