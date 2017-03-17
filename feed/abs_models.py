from abc import abstractmethod

from django.db import models
from core.abs_models import Authored

class Feedable(Authored):

    def feed_author(self):
        return self.author

    class Meta:
        abstract = True