# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-05-15 08:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=250)),
                ('description', models.TextField()),
                ('size', models.CharField(choices=[('4x6', '4x6'), ('5x7', '5x7'), ('8x8', '8x8'), ('11x4', '11x4'), ('12x12', '12x12'), ('8×10', '8×10'), ('5×15', '5×15'), ('12×36', '12×36'), ('8×24', '8×24'), ('16×20', '16×20'), ('20×30', '20×30')], default='4x6', max_length=10)),
                ('image', models.ImageField(upload_to='images')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
    ]
