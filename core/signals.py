from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import User
from .tasks import send_activation_email
from .helpers import send_mail


@receiver(post_save, sender=User)
def post_save_user_confirmation(instance, created=False, *args, **kwargs):
    if created:
        print 'Hello1'
        send_activation_email.apply_async([instance.id, ], countdown=5)
        #send_mail('so@admin.ru', instance)