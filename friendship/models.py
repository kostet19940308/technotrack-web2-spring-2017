from __future__ import unicode_literals

from django.db import models

from core.abs_models import Authored, CreatedAt, UpdatedAt
from core.models import User
from feed.abs_models import Feedable
from like.abs_models import Likeable

class FriendShip(Authored, CreatedAt, UpdatedAt, Feedable, Likeable):
    recipient = models.ForeignKey(User, related_name='new_friend')
    approved = models.BooleanField()

    def feed_author(self):
        return self.author


class Friends(Authored):
    friend_ship = models.ForeignKey(FriendShip)
    friend = models.ForeignKey(User, related_name="friend")
