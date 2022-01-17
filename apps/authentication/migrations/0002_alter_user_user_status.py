# Generated by Django 4.0 on 2022-01-12 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_status',
            field=models.CharField(choices=[('first_login', 'First Login'), ('active', 'Active'), ('not_active', 'Not Active'), ('suspended', 'Suspended'), ('blocked', 'Blocked'), ('deleted', 'Deleted')], max_length=100, verbose_name='User Status'),
        ),
    ]
