# Generated by Django 3.1.3 on 2020-12-01 16:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monapp', '0002_auto_20201201_1608'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='album',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='contact',
        ),
        migrations.DeleteModel(
            name='Album',
        ),
        migrations.DeleteModel(
            name='Artist',
        ),
        migrations.DeleteModel(
            name='Booking',
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
    ]
