# Generated by Django 3.2 on 2024-10-16 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuarios',
            old_name='id_usuario',
            new_name='id',
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='date_joined',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]
