from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(
        max_length=250, default="")
    description = models.TextField()
    size_choices = [
                    ('4x6', "4x6"),
                    ('5x7', '5x7'),
                    ('8x8', '8x8'),
                    ('11x4', '11x4'),
                    ('12x12', '12x12'),
                    ('8×10', '8×10'),
                    ('5×15', '5×15'),
                    ('12×36', '12×36'),
                    ('8×24', '8×24'),
                    ('16×20', '16×20'),
                    ('20×30', '20×30')]
    size = models.CharField(
        max_length=10,
        choices=size_choices, 
        default='4x6')
    image = models.ImageField(upload_to='images')
    price = models.DecimalField(
        max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name
