
from django.conf import settings
from templated_email import send_templated_mail, get_templated_mail, InlineImage


def send_mail(from_email, user):
    recipient_list = [user.email, ]
    if settings.DEBUG:
        recipient_list = [admin[0] for admin in settings.ADMINS]

    email = get_templated_mail('mail', {
        'image': InlineImage('avatar.jpg', open('./static/avatar.jpg', 'rb').read(), 'jpg'),
        'user': user,
    }, from_email, recipient_list)
    email.send()