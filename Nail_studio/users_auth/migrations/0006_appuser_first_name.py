# Generated by Django 4.2.3 on 2023-08-05 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_auth', '0005_remove_appuser_first_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='appuser',
            name='first_name',
            field=models.CharField(default='sample', max_length=30),
        ),
    ]
