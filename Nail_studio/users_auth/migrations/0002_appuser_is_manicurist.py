# Generated by Django 4.2.3 on 2023-07-28 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_auth', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appuser',
            name='is_manicurist',
            field=models.BooleanField(default=False),
        ),
    ]
