# Generated by Django 4.0.3 on 2022-04-06 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0008_alter_agentshift_slug_alter_businesstype_other_flag_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agentshift',
            name='slug',
            field=models.SlugField(blank=True, default='4qjwu20062q1fl920u0b4-4hmrbn0r1-nm', null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='businesstype',
            name='slug',
            field=models.SlugField(blank=True, default='b0-xd0w1ago420rr2zx7i42004ja6ojo3', null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='purchase_status',
            field=models.CharField(choices=[('paid', 'Paid'), ('pending', 'Pending'), ('trial', 'Trial')], max_length=40),
        ),
        migrations.AlterField(
            model_name='customer',
            name='slug',
            field=models.SlugField(blank=True, default='q1m4x6qn02dm4v0evv-e3u0f52l42r0bs', null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='customeragent',
            name='slug',
            field=models.SlugField(blank=True, default='62vj-d-bd042usyv0i1wca0r4a049f2ip5', null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='customeragentshift',
            name='slug',
            field=models.SlugField(blank=True, default='40r9w0q0o-1xy24or-y68xn2w405i2lti1', null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='customeragentshiftsattendant',
            name='slug',
            field=models.SlugField(blank=True, default='hdbf2r00p930-24pv15avrblv-62m44x03', null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='customercall',
            name='slug',
            field=models.SlugField(blank=True, default='9e06g19x4j200-h5-w0gq2r402p4cks0tb', null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='customercallparticipant',
            name='slug',
            field=models.SlugField(blank=True, default='42c206iv07r-152-0bfl44fuue00a0pmzx', null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='customerpackage',
            name='slug',
            field=models.SlugField(blank=True, default='118fg4f2-9z26ntl0841q902m45w900px', null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='customerpackageservice',
            name='slug',
            field=models.SlugField(blank=True, default='a29xv0b22l-rk0kioy0a1460-9rm04c14n', null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='customerpayment',
            name='slug',
            field=models.SlugField(blank=True, default='60j0w2he2sqnm10v0ps-244g40s4osjrm', null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='customerteam',
            name='slug',
            field=models.SlugField(blank=True, default='k6t30rl4g2fj4hczs-064-we122wza006m', null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='customertelecomnumber',
            name='slug',
            field=models.SlugField(blank=True, default='y012k2p-40-64q0oc22uqwjqqkar0udz4h', null=True, unique=True),
        ),
    ]
