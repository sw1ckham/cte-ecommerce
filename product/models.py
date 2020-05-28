from django.db import models
# from multiselectfield import MultiSelectField
from django_resized import ResizedImageField
from django.contrib.auth.models import User


# Create your models here.

class Product(models.Model):
    name = models.CharField(
        max_length=250, default="")
    description = models.TextField(max_length=200)
    size_choices = [
                    ('4x4', '4x6'),
                    ('5x7', '5x7'),
                    ('8x8', '8x8'),
                    ('11x4', '11x4'),
                    ('12x12', '12x12'),
                    ('8x10', '8×10'),
                    ('5x15', '5×15'),
                    ('12x36', '12×36'),
                    ('8x24', '8×24'),
                    ('16x20', '16×20'),
                    ('20x30', '20×30')
    ]
    size = models.CharField(
        choices=size_choices, max_length=10, default=1)
    image = ResizedImageField(size=[800, 800], quality=90, upload_to='images')
    CAT_CHOICES = [
        ('paper', 'Paper'),
        ('canvas', 'Canvas')
    ]
    catergorie = models.CharField(max_length=10, choices=CAT_CHOICES, default='canvas')
    price = models.DecimalField(
        max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name
    
