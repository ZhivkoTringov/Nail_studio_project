# Generated by Django 4.2.3 on 2023-08-09 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0005_service_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='duration',
            field=models.PositiveIntegerField(),
        ),
    ]