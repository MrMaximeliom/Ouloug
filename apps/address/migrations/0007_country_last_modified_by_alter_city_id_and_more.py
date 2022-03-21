# Generated by Django 4.0.2 on 2022-03-20 22:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('address', '0006_alter_city_slug_alter_country_slug_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='last_modified_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='last_user_modified_country', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='city',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='city',
            name='slug',
            field=models.SlugField(blank=True, default='49sx91vwvkjkdtgpxqcd', null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='country',
            name='slug',
            field=models.SlugField(blank=True, default='6yaywgzgbyivj6j6yhhe', null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='currency',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='currency',
            name='slug',
            field=models.SlugField(blank=True, default='zafdiyjt3vlvpwplv14c', null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='state',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='state',
            name='slug',
            field=models.SlugField(blank=True, default='qgrbemulwrqnh84pxjng', null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='usercountry',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='usercountry',
            name='slug',
            field=models.SlugField(blank=True, default='esldgf4hu6wo4vhyhery', null=True, unique=True),
        ),
    ]