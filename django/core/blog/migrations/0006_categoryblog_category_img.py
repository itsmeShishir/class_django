# Generated by Django 5.1.1 on 2024-09-22 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_blog_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoryblog',
            name='category_img',
            field=models.ImageField(blank=True, null=True, upload_to='categoryBlog_img/'),
        ),
    ]
