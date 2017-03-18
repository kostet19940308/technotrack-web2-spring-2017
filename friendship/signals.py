from __future__ import unicode_literals
from .models import Friends, FriendShip
from award.models import friendship, Award
from django.db.models.signals import post_init, post_save
from django.dispatch import receiver


def approve_friendship_post_init(sender, instance, **kwargs):
    instance.old_approved = instance.approved


def approve_friendship_post(sender, instance, **kwargs):
    if instance.approved and instance.old_approved != instance.approved:
        Friends.objects.create(friend_ship=instance, author=instance.author, friend=instance.recipient)
        Friends.objects.create(friend_ship=instance, author=instance.recipient, friend=instance.author)

@receiver(signal=post_save, sender=Friends)
def award_for_friends(instance, **kwargs):
    num = Friends.objects.filter(author=instance.author).count()
    if num in friendship.keys():
        Award.objects.create(
            author = instance.author,
            title = friendship[num],
            text = "{0} now have {1} friends".format(instance.author.username, num)
        )

post_init.connect(approve_friendship_post_init, sender=FriendShip, dispatch_uid="friendship_approve_friendship_pre")
post_save.connect(approve_friendship_post, sender=FriendShip, dispatch_uid="friendship_approve_friendship_post")
