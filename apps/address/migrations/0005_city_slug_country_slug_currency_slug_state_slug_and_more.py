# Generated by Django 4.0.2 on 2022-03-20 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0004_merge_20220301_1050'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='slug',
            field=models.SlugField(blank=True, default='injyrdokbplpjps6sqxu', null=True),
        ),
        migrations.AddField(
            model_name='country',
            name='slug',
            field=models.SlugField(blank=True, default='xnpytzzdh5ghbkyf9og6', null=True),
        ),
        migrations.AddField(
            model_name='currency',
            name='slug',
            field=models.SlugField(blank=True, default='fazc86n5r29lldu50nny', null=True),
        ),
        migrations.AddField(
            model_name='state',
            name='slug',
            field=models.SlugField(blank=True, default='emmsxiqfajp4mrxz0s8l', null=True),
        ),
        migrations.AddField(
            model_name='usercountry',
            name='slug',
            field=models.SlugField(blank=True, default='n2uozthdnd1ofltq8lvs', null=True),
        ),
    ]