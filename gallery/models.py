from django.db import models
from django_resized import ResizedImageField

# Create your models here.

class Art(models.Model):
    CAT_CHOICES = [
        ('paper', 'Paper'),
        ('canvas', 'Canvas')
    ]
    name = models.CharField(
        max_length=20)
    description = models.CharField(max_length=200)
    image = ResizedImageField(size=[800, 800], quality=90, upload_to='images')
    catergorie = models.CharField(max_length=10, choices=CAT_CHOICES, default='canvas')

    def __str__(self):
        return self.name
