# Generated by Django 4.2 on 2024-08-18 15:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_payment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='payment',
            options={'verbose_name': 'Платеж', 'verbose_name_plural': 'Платежи'},
        ),
    ]
