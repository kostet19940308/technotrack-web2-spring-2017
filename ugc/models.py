from __future__ import unicode_literals

from django.db import models
from core.models import User
from core.abs_models import Authored, CreatedAt, UpdatedAt
from feed.abs_models import Feedable
from like.abs_models import Likeable



class Post(CreatedAt, UpdatedAt, Feedable, Likeable):
    title = models.CharField(max_length=255)
    text = models.TextField(max_length=2048)

    def get_text_of_feed(self):
        return self.author.username + ' make new post: ' + self.title


