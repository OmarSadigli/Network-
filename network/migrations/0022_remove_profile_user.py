# Generated by Django 4.0.2 on 2022-04-06 12:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0021_profile_username_alter_profile_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
    ]
