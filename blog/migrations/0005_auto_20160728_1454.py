# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-28 05:54
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20160728_1447'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='created_at',
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(help_text='Markdown 문법을 써주세요'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(3)]),
        ),
    ]
