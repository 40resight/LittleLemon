# Generated by Django 4.2 on 2023-06-27 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurant', '0004_rename_booking_id_booking_id_rename_menu_id_menu_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='ID',
            field=models.SmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='booking',
            name='no_of_guests',
            field=models.SmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='menu',
            name='ID',
            field=models.SmallIntegerField(),
        ),
    ]
