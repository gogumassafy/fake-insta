# Generated by Django 2.1.8 on 2019-04-17 13:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='nicknamae',
            new_name='nickname',
        ),
    ]