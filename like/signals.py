from django.dispatch import receiver
from django.db.models import signals

from .models import Like
from award.models import Award, like_post, like_user
from ugc.models import Post

@receiver(signals.post_save, sender = Like)
def feed_and_award_for_like(instance, created, **kwargs):
    target = instance.target_object
    if created:
        num = target.likes_count()
        if num in like_post.keys():
            Award.objects.create(
                author=instance.author,
                title=like_post[num],
                text="You post {0} now have {1} likes".format(target.title, num)
            )

        num = 0
        for post in Post.objects.filter(author=target.author).all():
            num += post.likes_count()
        if num in like_user.keys():
            Award.objects.create(
                author=instance.author,
                title=like_post[num],
                text="You posts now have {1} likes".format(num)
            )
