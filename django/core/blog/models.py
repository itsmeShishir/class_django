from django.db import models

# Create your models here.
class CategoryBlog(models.Model):
    title = models.CharField(max_length=255)
    category_img = models.ImageField(upload_to="categoryBlog_img/", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Blog(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(CategoryBlog, on_delete=models.CASCADE, null = True, blank=True)
    image = models.ImageField(upload_to="blog_img/", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id} - {self.title}"