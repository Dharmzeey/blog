from django.db import models
from django.contrib.auth import settings
from ckeditor.fields import RichTextField

User = settings.AUTH_USER_MODEL

# Create your models here.
class Blog(models.Model):
  category_choices = (
    (1, "Livestyle"),
    (2, "Trading"),
    (3, "Programming"),
  )
  
  owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_owner")
  category = models.CharField(max_length=10, choices=category_choices)
  title = models.CharField(max_length=100)
  body = RichTextField()
  date_created = models.DateTimeField(auto_now_add=True)
  date_updated = models.DateTimeField(auto_now=True)
  
  class Meta:
    ordering = ["date_created"]
  def __str__(self):
    return self.title