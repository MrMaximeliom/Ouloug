# Generated by Django 4.0.2 on 2022-03-01 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='status',
            field=models.CharField(choices=[('active', 'active'), ('not_active', 'not active')], max_length=30),
        ),
    ]
