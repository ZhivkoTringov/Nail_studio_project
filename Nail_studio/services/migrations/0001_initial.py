# Generated by Django 4.2.3 on 2023-07-26 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categories', models.CharField(choices=[('Нокти', 'Нокти'), ('Мигли', 'Мигли'), ('Кола маска', 'Кола маска'), ('Лице', 'Лице'), ('Други', 'Други')], max_length=50)),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
            options={
                'permissions': [('manage_services', 'Can manage services')],
            },
        ),
    ]