from django.db import models
from core.models import User
from django.utils import timezone

class Authored(models.Model):
    author =  models.ForeignKey(User);

    class Meta:
        abstract = True;


class CreatedAt(models.Model):
    created_at = models.DateTimeField(default=timezone.now, blank=True);

    class Meta:
        abstract = True;


class UpdatedAt(models.Model):
    updated_at = models.DateTimeField(auto_now=True, blank=True);

    class Meta:
        abstract = True;


class Titled(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        abstract = True;

