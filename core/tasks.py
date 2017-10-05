from celery import task
from .models import User
from .helpers import send_mail

@task(bind=True, default_retry_delay=10)
def send_activation_email(self, user_id):
    user = User.objects.get(id=user_id)
    try:
        send_mail(user)
    except Exception as exc:
        raise self.retry(exc=exc)