# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-15 14:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0016_remove_jeux_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='jeux',
            name='image',
            field=models.ImageField(default=1, upload_to='photos_jeux/', verbose_name='Image'),
            preserve_default=False,
        ),
    ]
