# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-12 06:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='upload',
            field=models.ImageField(upload_to='media/uploads'),
        ),
    ]
