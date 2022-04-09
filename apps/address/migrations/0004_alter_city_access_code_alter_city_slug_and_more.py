# Generated by Django 4.0.3 on 2022-04-09 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0003_alter_city_slug_alter_country_arabic_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='access_code',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='city',
            name='slug',
            field=models.SlugField(blank=True, default='m72u31h48jznlz-2o-00stkrm930m429d2', null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='access_code',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='country',
            name='slug',
            field=models.SlugField(blank=True, default='t2x00fz9w4v-n6o3s0h19742f5j41-2sxk', null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='currency',
            name='slug',
            field=models.SlugField(blank=True, default='242u2zmi04t-ck7ggde7qa9x9k3x001kp', null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='state',
            name='slug',
            field=models.SlugField(blank=True, default='2swu3-dnk024qz1kqe0xxhn0474-h2ia9y', null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='usercountry',
            name='slug',
            field=models.SlugField(blank=True, default='299ilmah3e4p0l-941ga227zt0qqc30x-r', null=True, unique=True),
        ),
    ]
