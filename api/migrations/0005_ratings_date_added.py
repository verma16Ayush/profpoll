# Generated by Django 3.1.5 on 2021-02-02 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20210201_1904'),
    ]

    operations = [
        migrations.AddField(
            model_name='ratings',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
