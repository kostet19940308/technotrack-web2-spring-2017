from __future__ import unicode_literals

from django.db import models
from core.models import User
from core.abs_models import Authored, CreatedAt, UpdatedAt, Likeable
from feed.abs_models import Feedable
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class Post(Authored, CreatedAt, UpdatedAt, Feedable, Likeable):
    title = models.CharField(max_length=255)
    text = models.TextField(max_length=2048)

    def feed_author(self):
        return self.author


class Like(Authored, CreatedAt, UpdatedAt):
    target_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    target_id = models.PositiveIntegerField()
    target_object = GenericForeignKey('target_type', 'target_id')

    class Meta:
        unique_together = ("target_type", "target_id", "author")
