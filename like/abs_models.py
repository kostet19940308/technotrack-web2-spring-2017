from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from .models import Like



class Likeable(models.Model):

    likes = GenericRelation(
        Like,
        content_type_field='target_type',
        object_id_field='target_id'
    )

    def likes_count(self):
        return self.likes.count()

    class Meta:
        abstract = True