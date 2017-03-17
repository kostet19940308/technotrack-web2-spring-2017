from __future__ import unicode_literals

from django.db import models
from core.abs_models import Authored, CreatedAt, UpdatedAt
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType



class Like(Authored, CreatedAt, UpdatedAt):
    target_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    target_id = models.PositiveIntegerField()
    target_object = GenericForeignKey('target_type', 'target_id')

    class Meta:
        unique_together = ("target_type", "target_id", "author")