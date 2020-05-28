# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-05-28 09:50
from __future__ import unicode_literals

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0012_auto_20200527_2013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=django_resized.forms.ResizedImageField(crop=None, force_format=None, keep_meta=True, quality=90, size=[400, 600], upload_to='images'),
        ),
    ]
