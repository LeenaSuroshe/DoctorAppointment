# Generated by Django 4.1.5 on 2023-01-11 13:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DocApp', '0015_appointment_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='user',
        ),
    ]
