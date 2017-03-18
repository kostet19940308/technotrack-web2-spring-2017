# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-18 15:21
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='members',
            field=models.ManyToManyField(related_name='chat_members', to=settings.AUTH_USER_MODEL),
        ),
    ]