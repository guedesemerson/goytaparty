# Generated by Django 2.2.11 on 2020-03-15 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('convidado', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='convidado',
            name='identidade',
            field=models.CharField(blank=True, max_length=9, null=True),
        ),
    ]
