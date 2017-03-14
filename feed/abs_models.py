from abc import abstractmethod

from django.db import models

class Feedable(models.Model):

    @abstractmethod
    def feed_author(self):
        pass

    class Meta:
        abstract = True