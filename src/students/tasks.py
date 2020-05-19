from celery import shared_task


@shared_task
def delete_logs():
    from django.utils import timezone
    from datetime import timedelta
    from students.models import Logger

    now = timezone.now()
    last_day = now - timedelta(days=7)
    Logger.objects.filter(created__lte=last_day).delete()


@shared_task
def send_mail(request):
    from django.core.mail import send_mail
    send_mail(request.get('title'),
              request.get('message'),
              'testdjangohillel@gmail.com',
              [request.get('email_from')])
