# Generated by Django 4.2.3 on 2023-07-29 08:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0006_rename_usermodel_manicurist_manicurist_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='manicurist',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='appointments.manicurist'),
        ),
    ]
