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
        migrations.AddField(
            model_name='usercountry',
            name='added_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='added_by_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='usercountry',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='address.country'),
        ),
        migrations.AddField(
            model_name='usercountry',
            name='last_modified_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='last_modified_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='usercountry',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='state',
            name='added_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_added_state', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='state',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='address.country'),
        ),
        migrations.AddField(
            model_name='state',
            name='last_modified_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='last_user_modified_state', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='currency',
            name='added_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_added_currency', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='currency',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='address.country'),
        ),
        migrations.AddField(
            model_name='currency',
            name='last_modified_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='last_user_modified_currency', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='country',
            name='added_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_added_country', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='country',
            name='last_modified_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='last_user_modified_country', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='city',
            name='added_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_added_city', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='city',
            name='last_modified_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='last_user_modified_city', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='city',
            name='state',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='address.state'),
        ),
    ]
