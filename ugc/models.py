from __future__ import unicode_literals

from django.db import models
from core.models import User
from core.abs_models import Authored, CreatedAt, UpdatedAt


class Post(Authored, CreatedAt, UpdatedAt):
    title = models.CharField(max_length=255)
    text = models.TextField(max_length=2048)
