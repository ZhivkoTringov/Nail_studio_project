# Generated by Django 4.2.3 on 2023-07-29 12:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0009_appointment_client_first_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='manicurist',
        ),
        migrations.DeleteModel(
            name='Manicurist',
        ),
    ]
