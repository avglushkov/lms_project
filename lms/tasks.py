from celery import shared_task
from config.settings import EMAIL_HOST_USER
from django.core.mail import send_mail

from lms.models import Subscription
from users.models import User


@shared_task
def change_course_sendmail(course, serializer='json'):
    """задание отправки письма подписчикам курса при обновлении"""

    subscriptions = Subscription.objects.filter(course=course)
    recipient_list = [subs.user.email for subs in subscriptions]
    send_mail(
        subject='В курсе произошли изменения',
        message=f'В курсе "{course.name}" произошли изменения',
        from_email=EMAIL_HOST_USER,
        recipient_list=recipient_list,
        fail_silently=True
    )

