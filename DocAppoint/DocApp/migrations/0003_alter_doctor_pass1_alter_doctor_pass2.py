# Generated by Django 4.1.3 on 2023-01-01 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DocApp', '0002_alter_doctor_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='pass1',
            field=models.TextField(max_length=20),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='pass2',
            field=models.TextField(max_length=20),
        ),
    ]
