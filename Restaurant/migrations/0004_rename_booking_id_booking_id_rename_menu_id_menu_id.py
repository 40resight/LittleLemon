# Generated by Django 4.2 on 2023-06-27 20:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurant', '0003_rename_id_booking_booking_id_rename_id_menu_menu_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='Booking_ID',
            new_name='ID',
        ),
        migrations.RenameField(
            model_name='menu',
            old_name='Menu_ID',
            new_name='ID',
        ),
    ]