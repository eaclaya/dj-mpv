# Generated by Django 5.0.6 on 2024-06-11 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0002_alter_client_due_date_alter_client_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='due_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
