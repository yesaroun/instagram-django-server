# Generated by Django 4.1.7 on 2023-02-22 02:26

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="user",
            old_name="followerNumber",
            new_name="followerNum",
        ),
    ]
