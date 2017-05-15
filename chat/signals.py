from .models import ChatMembership, Chat
from django.db.models.signals import post_save


def add_author_in_chart(instance, created=False, *args, **kwargs):
    if created:
        ChatMembership.objects.create(chat=instance, user=instance.author, inviter=instance.author)

post_save.connect(add_author_in_chart, sender=Chat)