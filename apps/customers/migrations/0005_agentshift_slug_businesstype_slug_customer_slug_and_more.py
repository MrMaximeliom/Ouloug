# Generated by Django 4.0.3 on 2022-03-21 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0004_delete_busnesstype'),
    ]

    operations = [
        migrations.AddField(
            model_name='agentshift',
            name='slug',
            field=models.SlugField(blank=True, default='3e6fdjrjzo5choojo6ah', null=True, unique=True),
        ),
        migrations.AddField(
            model_name='businesstype',
            name='slug',
            field=models.SlugField(blank=True, default='tcdkqdk8gv5txrosdbdy', null=True, unique=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='slug',
            field=models.SlugField(blank=True, default='ubo1zridoasrcgjm1er7', null=True, unique=True),
        ),
        migrations.AddField(
            model_name='customeragent',
            name='slug',
            field=models.SlugField(blank=True, default='cix9x5azb7eaaarblomu', null=True, unique=True),
        ),
        migrations.AddField(
            model_name='customeragentshift',
            name='slug',
            field=models.SlugField(blank=True, default='mj8wdrplccbyzjraqrb8', null=True, unique=True),
        ),
        migrations.AddField(
            model_name='customeragentshiftsattendant',
            name='slug',
            field=models.SlugField(blank=True, default='v1s4aslzze1k50dcimhu', null=True, unique=True),
        ),
        migrations.AddField(
            model_name='customercall',
            name='slug',
            field=models.SlugField(blank=True, default='1xq426dfl9r596bpjuyy', null=True, unique=True),
        ),
        migrations.AddField(
            model_name='customercallparticipant',
            name='slug',
            field=models.SlugField(blank=True, default='cbo528aub8nqc29echr5', null=True, unique=True),
        ),
        migrations.AddField(
            model_name='customerpackage',
            name='slug',
            field=models.SlugField(blank=True, default='kfo02ihultwerwd7z0o5', null=True, unique=True),
        ),
        migrations.AddField(
            model_name='customerpackageservice',
            name='slug',
            field=models.SlugField(blank=True, default='c8hmlgpqcj2rgoszon2w', null=True, unique=True),
        ),
        migrations.AddField(
            model_name='customerpayment',
            name='slug',
            field=models.SlugField(blank=True, default='fgwazdormsfijcoglscv', null=True, unique=True),
        ),
        migrations.AddField(
            model_name='customerteam',
            name='slug',
            field=models.SlugField(blank=True, default='72ldrse8gdipwujlp74p', null=True, unique=True),
        ),
        migrations.AddField(
            model_name='customertelecomnumber',
            name='slug',
            field=models.SlugField(blank=True, default='ewwi7jpp620ipjcjnzyw', null=True, unique=True),
        ),
    ]