# Generated by Django 4.2.3 on 2023-08-11 15:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_remove_galleryphoto_name_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='galleryphoto',
            options={'permissions': [('manage_photos', 'Can manage photos')]},
        ),
    ]