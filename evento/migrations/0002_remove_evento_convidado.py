# Generated by Django 2.2.11 on 2020-03-07 22:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('evento', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evento',
            name='convidado',
        ),
    ]
