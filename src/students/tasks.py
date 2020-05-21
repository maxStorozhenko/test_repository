from datetime import timedelta

from celery import shared_task

from django.core.mail import send_mail
from django.utils import timezone

from students.models import Logger


@shared_task
def delete_logs():
    now = timezone.now()
    last_day = now - timedelta(days=7)
    Logger.objects.filter(created__lte=last_day).delete()


@shared_task
def send_email(request):
    send_mail(request.get('title'),
              request.get('message'),
              'testdjangohillel@gmail.com',
              [request.get('email_from')])
