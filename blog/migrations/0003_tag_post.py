# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-28 05:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20160728_1351'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='post',
            field=models.ManyToManyField(to='blog.Post'),
        ),
    ]
