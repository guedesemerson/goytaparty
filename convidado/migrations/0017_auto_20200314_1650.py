# Generated by Django 2.2.11 on 2020-03-14 19:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('convidado', '0016_auto_20200314_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='convidado',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
