# Generated by Django 4.0.3 on 2022-03-26 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0007_alter_user_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='slug',
            field=models.SlugField(blank=True, default='t0uwagnldknd9edee4jqm', null=True, unique=True),
        ),
    ]
