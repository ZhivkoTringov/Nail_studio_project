# Generated by Django 4.2.3 on 2023-07-29 12:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('appointments', '0011_remove_appointment_client_appointment_manicurist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='manicurist',
        ),
        migrations.AddField(
            model_name='appointment',
            name='client',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]