from django.db import models
from multiselectfield import MultiSelectField
from django_resized import ResizedImageField
from django.contrib.auth.models import User


# Create your models here.

class Product(models.Model):
    name = models.CharField(
        max_length=250, default="")
    description = models.TextField(max_length=200)
    size_choices = [
                    (1 , '4x6'),
                    (2 , '5x7'),
                    (3, '8x8'),
                    (4, '11x4'),
                    (5, '12x12'),
                    (6, '8×10'),
                    (7, '5×15'),
                    (8, '12×36'),
                    (9, '8×24'),
                    (10, '16×20'),
                    (11, '20×30')
    ]
    size = MultiSelectField(
        choices=size_choices)
    image = ResizedImageField(size=[800, 600], quality=90, upload_to='images')
    CAT_CHOICES = [
        ('paper', 'Paper'),
        ('canvas', 'Canvas')
    ]
    catergorie = models.CharField(max_length=10, choices=CAT_CHOICES, default='canvas')
    price = models.DecimalField(
        max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name
    
