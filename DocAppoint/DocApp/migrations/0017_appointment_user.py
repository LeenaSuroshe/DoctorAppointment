# Generated by Django 4.1.5 on 2023-01-11 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DocApp', '0016_remove_appointment_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='user',
            field=models.CharField(max_length=100, null=True),
        ),
    ]