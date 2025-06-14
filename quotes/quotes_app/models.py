from django.db import models


# Create your models here.
class Quote(models.Model):
    quote = models.CharField(max_length=255)
    author = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
