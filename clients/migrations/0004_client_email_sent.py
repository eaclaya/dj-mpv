# Generated by Django 5.0.6 on 2024-06-13 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0003_alter_client_due_date_alter_client_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='email_sent',
            field=models.BooleanField(default=True),
        ),
    ]
