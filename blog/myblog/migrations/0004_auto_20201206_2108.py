# Generated by Django 3.1.3 on 2020-12-06 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0003_auto_20201204_1501'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Utilisateur',
        ),
        migrations.AddField(
            model_name='publication',
            name='archive',
            field=models.BooleanField(default=False),
        ),
    ]
