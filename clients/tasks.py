from celery import shared_task
from django.core.mail import send_mail
from django.utils import timezone
from django.utils.translation import gettext as _
from django.conf import settings
from .models import Client

@shared_task
def check_due_payments():
    now = timezone.now()
    clients = Client.objects.all(due_date__lte=now, email_sent=False)
    for client in clients:
        subject = _('Payment Due')
        message = _('Payment Due Email')
        sender = settings.DEFAULT_FROM_EMAIL
        send_mail(
            subject,
            message,
            sender,
            [client.email],
            fail_silently=False,
        )
        client.email_sent = True
        client.save()
