# Generated by Django 3.2 on 2024-11-04 18:49

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_auto_20241101_2328'),
    ]

    operations = [
        migrations.AddField(
            model_name='archivo',
            name='compartido_con',
            field=models.ManyToManyField(blank=True, related_name='archivos_compartidos', to=settings.AUTH_USER_MODEL),
        ),
    ]