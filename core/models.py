from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser
from django.db import models



class User(AbstractUser):

    status = models.CharField(max_length=255, blank=True)

    about_yourself = models.TextField(max_length=5000, blank=True)

