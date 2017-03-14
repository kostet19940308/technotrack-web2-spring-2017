from __future__ import unicode_literals

from django.db import models

from core.abs_models import Authored, CreatedAt, UpdatedAt
from core.models import User

class FriendShip(Authored, CreatedAt, UpdatedAt):
    #recipient = models.ForeignKey(User)
    approved = models.BooleanField()


class Friends(Authored):
    friend_ship = models.ForeignKey(FriendShip)
    friend = models.ForeignKey(User, related_name="friend")