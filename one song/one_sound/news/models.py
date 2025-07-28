from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    news_image = models.ImageField(upload_to='news_images/', blank=True, null=True)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    category = models.CharField(max_length=100, choices=[('Music', 'Music'), ('Events', 'Events & Press'), ('Festivals', 'Festivals'), ('Lifestyle', 'Lifestyle'), ('Other', 'Other')], default='Music')

    def __str__(self):
        return self.title