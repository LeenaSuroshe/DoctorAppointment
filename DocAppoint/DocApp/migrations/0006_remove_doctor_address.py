# Generated by Django 4.1.4 on 2023-01-02 12:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DocApp', '0005_remove_doctor_pass1_remove_doctor_pass2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='address',
        ),
    ]
