# Generated by Django 2.2.11 on 2020-03-11 22:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('evento', '0003_evento_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evento',
            name='user',
        ),
    ]
