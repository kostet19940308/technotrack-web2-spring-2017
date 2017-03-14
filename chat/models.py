from __future__ import unicode_literals

from django.db import models

from core.abs_models import Authored, CreatedAt
from core.models import User


class Chat(Authored, CreatedAt):
    name = models.CharField(max_length=255)
    members = models.ManyToManyField(User, related_name="charts")


class Message(Authored, CreatedAt):
    chat = models.ForeignKey(Chat)
    title = models.CharField(max_length=255)
    text = models.TextField(max_length=2048)

