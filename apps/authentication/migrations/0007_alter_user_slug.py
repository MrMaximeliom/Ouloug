# Generated by Django 4.0.3 on 2022-03-26 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0006_user_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='slug',
            field=models.SlugField(blank=True, default='jhrt1zqcxyxv68ic11bj', null=True),
        ),
    ]
