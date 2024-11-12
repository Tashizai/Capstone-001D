# Generated by Django 3.2 on 2024-11-01 23:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_rename_creador_carpeta_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='archivo',
            name='tamano',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='archivo',
            name='carpeta',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='archivos', to='app.carpeta'),
        ),
    ]
