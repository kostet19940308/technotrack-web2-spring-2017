from __future__ import unicode_literals

from django.apps import AppConfig


class FriendshipConfig(AppConfig):
    name = 'friendship'

    def ready(self):
        from . import signals
