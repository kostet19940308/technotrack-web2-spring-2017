from __future__ import unicode_literals
from core.abs_models import Authored, CreatedAt, UpdatedAt, Titled
from feed.abs_models import Feedable

from django.db import models


class Award( CreatedAt, UpdatedAt, Titled, Feedable):
    text = models.CharField(max_length=255)

    class Meta:
        unique_together = ('author', 'title')

    def get_text_of_feed(self):
        return '{0} take new award: {1}'.format(self.author, self.title)





friendship = {
    1 : 'First friend',
    5: 'Friendly',
    10: 'Popular',
    50: 'Sole of company'
}

like_post = {
    10: 'Interesting',
    20: 'Actual',
    50: 'Sensational'
}

like_user = {
    10: 'Someone watch you',
    50: 'You are interesting',
    100:'News channel'
}