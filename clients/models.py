from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=100)
    domain = models.CharField(max_length=100)
    due_date = models.DateField(blank=True, null=True)
    contact = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    email_sent = models.BooleanField(default=True)

    def __str__(self):
        return self.name
