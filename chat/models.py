from __future__ import unicode_literals

from django.db import models

from core.abs_models import Authored, CreatedAt, Titled
from core.models import User


class Chat(Authored, CreatedAt):
    name = models.CharField(max_length=255)
    members = models.ManyToManyField(User, related_name="chat_members")


class Message(Authored, CreatedAt,Titled):
    chat = models.ForeignKey(Chat)
    text = models.TextField(max_length=2048)

