# Generated by Django 3.1.6 on 2021-02-27 14:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geo', '0003_auto_20210227_1654'),
    ]

    operations = [
        migrations.RenameField(
            model_name='incidences',
            old_name='one',
            new_name='ones',
        ),
        migrations.RenameField(
            model_name='incidences',
            old_name='today',
            new_name='todays',
        ),
    ]