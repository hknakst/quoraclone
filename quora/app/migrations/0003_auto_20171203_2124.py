# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-03 21:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20171203_2002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tags',
            name='tag',
            field=models.SlugField(max_length=25),
        ),
    ]
