from django.db import models

# Create your models here.

class Art(models.Model):
    CAT_CHOICES = [
        ('paper', 'Paper'),
        ('canvas', 'Canvas')
    ]
    name = models.CharField(
        max_length=20)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')
    catergorie = models.CharField(max_length=10, choices=CAT_CHOICES, default='canvas')

    def __str__(self):
        return self.name
