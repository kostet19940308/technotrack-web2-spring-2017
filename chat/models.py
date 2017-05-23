from __future__ import unicode_literals

from django.db import models

from core.abs_models import Authored, CreatedAt, Titled
from core.models import User


class Chat(Authored, CreatedAt):
    name = models.CharField(max_length=255)
    members = models.ManyToManyField(
        User,
        related_name="chats",
        through="ChatMembership",
        through_fields=('chat', 'user'),
        verbose_name="chat members list"
    )


class Message(Authored, CreatedAt):
    chat = models.ForeignKey(Chat, related_name="messages")
    text = models.TextField(max_length=2048)
    title = models.CharField(max_length=255, blank=True)

class ChatMembership(CreatedAt):
    chat = models.ForeignKey(Chat)
    user = models.ForeignKey(User)
    inviter = models.ForeignKey(
        User,
        related_name="+",
        verbose_name="chat inviter"
    )

    class Meta:
        unique_together = (('user', 'chat'), )