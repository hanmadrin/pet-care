# Generated by Django 4.2.1 on 2023-07-29 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authentication", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="is_verified",
            field=models.BooleanField(default=True),
        ),
    ]
