# Generated by Django 4.2 on 2023-06-27 20:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurant', '0002_alter_menu_inventory'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='ID',
            new_name='Booking_ID',
        ),
        migrations.RenameField(
            model_name='menu',
            old_name='ID',
            new_name='Menu_ID',
        ),
    ]
