# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-16 15:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='about_yourself',
            field=models.TextField(blank=True, max_length=5000),
        ),
        migrations.AddField(
            model_name='user',
            name='status',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]