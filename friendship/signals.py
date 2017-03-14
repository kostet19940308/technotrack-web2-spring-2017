from .models import Friends, FriendShip
from django.db.models.signals import post_init, post_save


def approve_friendship_post_init(sender, instance, **kwargs):
    instance.old_approved = instance.approved


def approve_friendship_post(sender, instance, **kwargs):
    if instance.approved and instance.old_approved != instance.approved:
        Friends.objects.create(friend_ship=instance, author=instance.author, friend=instance.recipient)
        Friends.objects.create(friend_ship=instance, author=instance.recipient, friend=instance.author)

post_init.connect(approve_friendship_post_init, sender=FriendShip, dispatch_uid="friendship_approve_friendship_pre")
post_save.connect(approve_friendship_post, sender=FriendShip, dispatch_uid="friendship_approve_friendship_post")