from abc import abstractmethod

from django.db import models
from core.abs_models import Authored

class Feedable(Authored):

    @abstractmethod
    def get_text_of_feed(self):
        pass

    def feed_author(self):
        return self.author

    class Meta:
        abstract = True