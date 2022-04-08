# Generated by Django 4.0.3 on 2022-04-07 15:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('address', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, default='0xz2-3fya22h01d48lhxe-5n7oaz5sey0i', null=True, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('arabic_name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('arabic_description', models.CharField(max_length=200)),
                ('subscription_type', models.CharField(max_length=200)),
                ('status', models.CharField(choices=[('active', 'active'), ('not_active', 'not active')], max_length=30)),
                ('added_datetime', models.DateTimeField(auto_now=True)),
                ('last_modification_datetime', models.DateTimeField(auto_now_add=True)),
                ('added_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_added_service', to=settings.AUTH_USER_MODEL)),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='address.country')),
                ('last_modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='last_user_modified_service', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'service',
            },
        ),
    ]
