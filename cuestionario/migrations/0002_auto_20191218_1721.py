# Generated by Django 2.2.2 on 2019-12-18 20:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cuestionario', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cuestionario',
            name='mascota',
        ),
        migrations.AddField(
            model_name='cuestionario',
            name='usuario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
