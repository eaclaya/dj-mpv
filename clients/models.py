from django.db import models
from django.utils import timezone

class Client(models.Model):
    name = models.CharField(max_length=100)
    domain = models.CharField(max_length=100)
    due_date = models.DateField(blank=True, null=True)
    contact = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    email_sent = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.due_date is not None and self.due_date > timezone.now().date():
            self.email_sent = False
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
