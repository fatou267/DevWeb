# Generated by Django 3.1.3 on 2020-12-04 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Utilisateur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=25)),
                ('prenom', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=40)),
                ('telephone', models.IntegerField(max_length=12)),
                ('profession', models.CharField(max_length=50)),
                ('age', models.IntegerField(max_length=5)),
            ],
        ),
    ]
