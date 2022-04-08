# Generated by Django 4.0.3 on 2022-04-07 15:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('telecoms', '0001_initial'),
        ('packages', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('teams', '0001_initial'),
        ('address', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AgentShift',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, default='8bq9mb-0jh2q2ihg-21zgwm870x5854x0w', null=True, unique=True)),
                ('number', models.IntegerField()),
                ('name', models.CharField(max_length=200)),
                ('arabic_name', models.CharField(max_length=200)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('status', models.CharField(choices=[('active', 'Active'), ('not_active', 'Not Active')], max_length=10)),
                ('is_saturday_on', models.BooleanField()),
                ('is_sunday_on', models.BooleanField()),
                ('is_monday_on', models.BooleanField()),
                ('is_tuesday_on', models.BooleanField()),
                ('is_wednesday_on', models.BooleanField()),
                ('is_thursday_on', models.BooleanField()),
                ('is_friday_on', models.BooleanField()),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='address.country')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teams.team')),
            ],
            options={
                'db_table': 'agent_shift',
            },
        ),
        migrations.CreateModel(
            name='BusinessType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, default='29oivo1t455jo0t20pqv2-3b2q0-y7p8w7', null=True, unique=True)),
                ('type_name', models.CharField(max_length=240)),
                ('arabic_type_name', models.CharField(max_length=240)),
                ('other_flag', models.BooleanField()),
                ('added_datetime', models.DateTimeField(auto_now=True)),
                ('last_modification_datetime', models.DateTimeField(auto_now_add=True)),
                ('added_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_added_business_type_main', to=settings.AUTH_USER_MODEL)),
                ('last_modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='last_user_modified_business_type_main', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, default='mk2k2u0z5km4-5x-e5j1870zckxs20n5j0', null=True, unique=True)),
                ('business_name', models.CharField(max_length=224)),
                ('arabic_business_name', models.CharField(max_length=200)),
                ('business_shortname', models.CharField(max_length=50)),
                ('business_type_other', models.CharField(max_length=200)),
                ('business_address_one', models.CharField(max_length=200)),
                ('logo', models.ImageField(upload_to='customer_logo')),
                ('registration_number', models.IntegerField()),
                ('established_date', models.DateField(max_length=200)),
                ('admin_mobile_number', models.CharField(max_length=40)),
                ('account_status', models.CharField(choices=[('not_confirmed', 'Not Confirmed'), ('active', 'Active'), ('suspended', 'Suspended'), ('closed', 'Closed'), ('blocked', 'Blocked'), ('dormant', 'Dormant'), ('stopped', 'Stopped')], max_length=80)),
                ('purchase_status', models.CharField(choices=[('paid', 'Paid'), ('pending', 'Pending'), ('trial', 'Trial')], max_length=40)),
                ('email', models.EmailField(max_length=200)),
                ('expiry_datetime', models.DateTimeField()),
                ('effective_datetime', models.DateTimeField(auto_now=True)),
                ('added_datetime', models.DateTimeField(auto_now_add=True, null=True)),
                ('business_address_city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='address.city')),
                ('business_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='customers.businesstype')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='customer', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'customer',
            },
        ),
        migrations.CreateModel(
            name='CustomerAgent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, default='sax29-70y5hpvi1040w-52wmp0xtg258uf', null=True, unique=True)),
                ('extension_number', models.CharField(max_length=140)),
                ('first_work_address', models.CharField(max_length=200)),
                ('second_work_address', models.CharField(max_length=200)),
                ('account_status', models.CharField(choices=[('not_confirmed', 'Not Confirmed'), ('active', 'Active'), ('suspended', 'Suspended'), ('closed', 'Closed'), ('blocked', 'Blocked'), ('dormant', 'Dormant'), ('stopped', 'Stopped')], max_length=40)),
                ('login_status', models.CharField(choices=[('login', 'Login'), ('logout', 'Logout'), ('break', 'Break'), ('busy', 'Busy'), ('on_leave', 'On leave')], max_length=10)),
                ('added_datetime', models.DateTimeField(auto_now=True)),
                ('last_modification_datetime', models.DateTimeField(auto_now_add=True)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='address.city')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teams.team')),
            ],
            options={
                'db_table': 'customer_agent',
            },
        ),
        migrations.CreateModel(
            name='CustomerAgentShift',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, default='jm-7natus0s2i2q0x1d-xmr2p57l80b54a', null=True, unique=True)),
                ('shift_number', models.CharField(max_length=200)),
                ('shift_name', models.CharField(max_length=200)),
                ('arabic_shift_name', models.CharField(max_length=200)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('status', models.BooleanField()),
                ('agent_shift', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='customers.agentshift')),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='customers.customer')),
            ],
            options={
                'db_table': 'customer_agent_shift',
            },
        ),
        migrations.CreateModel(
            name='CustomerCall',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, default='b20xc1klsa70hn528vf6-0-cne02f5814g', null=True, unique=True)),
                ('call_datetime', models.DateTimeField(auto_now=True)),
                ('login_status', models.CharField(choices=[('login', 'Login'), ('logout', 'Logout'), ('break', 'Break'), ('busy', 'Busy'), ('on_leave', 'On leave')], max_length=80)),
                ('call_direction', models.CharField(choices=[('inbound', 'Inbound'), ('outbound', 'Outbound')], max_length=40)),
                ('call_type', models.CharField(choices=[('normal', 'Normal'), ('group', 'Group')], max_length=40)),
                ('call_duration', models.TimeField(auto_now_add=True)),
                ('start_time', models.TimeField(auto_now=True)),
                ('end_time', models.TimeField()),
                ('status', models.CharField(choices=[('complete', 'Complete'), ('not_answered', 'Not Answered'), ('rejected', 'Rejected'), ('busy', 'Busy'), ('waiting', 'Waiting'), ('not_completed', 'Not Completed')], max_length=80)),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='address.country')),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='customers.customer')),
                ('customer_agent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='customers.customeragent')),
            ],
            options={
                'db_table': 'customer_call',
            },
        ),
        migrations.CreateModel(
            name='CustomerPackage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, default='gu908f50q8t-hjdvgfi0r9-qh52229l174', null=True, unique=True)),
                ('subscription_amount', models.DecimalField(decimal_places=10, max_digits=12)),
                ('due_amount', models.DecimalField(decimal_places=10, max_digits=12)),
                ('customer_package_datetime', models.DateTimeField(auto_now=True)),
                ('effective_date', models.DateField()),
                ('expiry_date', models.DateTimeField()),
                ('delete_date', models.DateTimeField()),
                ('subscription_status', models.CharField(choices=[('active', 'Active'), ('trial', 'Trial'), ('suspended', 'Suspended'), ('not_paid', 'Not Paid'), ('deleted', 'Deleted')], max_length=40)),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='address.currency')),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='customers.customer')),
                ('package', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='packages.package')),
                ('package_billing_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='packages.packagebillingtype')),
            ],
            options={
                'db_table': 'customer_package',
            },
        ),
        migrations.CreateModel(
            name='CustomerTelecomNumber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, default='50un234u8-2pnlg-07g2t60h0p51ty8sma', null=True, unique=True)),
                ('actual_telephone_number', models.CharField(max_length=80)),
                ('memo', models.TextField()),
                ('taken_date', models.DateTimeField()),
                ('withdraw_date', models.DateTimeField()),
                ('status', models.CharField(choices=[('active', 'Active'), ('stop', 'Stop'), ('withdraw', 'Withdraw')], max_length=50)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.customer')),
                ('telecom_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='telecoms.telecomnumber')),
            ],
            options={
                'db_table': 'customer_telecom_number',
            },
        ),
        migrations.CreateModel(
            name='CustomerTeam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, default='5k1-mp7lz020r4d400rnjqmj8m-2uef225', null=True, unique=True)),
                ('address_one', models.CharField(max_length=200)),
                ('address_second', models.CharField(max_length=200)),
                ('status', models.CharField(choices=[('active', 'Active'), ('not_active', 'Not Active')], max_length=40)),
                ('added_datetime', models.DateTimeField(auto_now=True)),
                ('last_modification_datetime', models.DateTimeField(auto_now_add=True)),
                ('added_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_added_customer_team', to=settings.AUTH_USER_MODEL)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='address.city')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.customer')),
                ('last_modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='last_user_modified_customer_team', to=settings.AUTH_USER_MODEL)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teams.team')),
            ],
            options={
                'db_table': 'customer_team',
            },
        ),
        migrations.CreateModel(
            name='CustomerPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, default='2to-v4t0i904-h20a8d572tfw5nhs5x1rk', null=True, unique=True)),
                ('transaction_datetime', models.DateTimeField(auto_now=True)),
                ('transaction_amount', models.DecimalField(decimal_places=10, max_digits=12)),
                ('payment_type', models.CharField(max_length=100)),
                ('status', models.BooleanField()),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='address.currency')),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='customers.customer')),
                ('customer_package', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='packages.package')),
            ],
            options={
                'db_table': 'customer_payment',
            },
        ),
        migrations.CreateModel(
            name='CustomerPackageService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, default='gk8n00wqtsa7l215xw-2452no3y20wlbx', null=True, unique=True)),
                ('subscription_type_value', models.IntegerField()),
                ('service_price', models.DecimalField(decimal_places=10, max_digits=12)),
                ('total_price', models.DecimalField(decimal_places=10, max_digits=12)),
                ('currency_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='address.currency')),
                ('customer_package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.customerpackage')),
                ('package_service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='packages.packageservice')),
            ],
            options={
                'db_table': 'customer_package_service',
            },
        ),
        migrations.CreateModel(
            name='CustomerCallParticipant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, default='2by2e52p5ua5-0-v7lkc0o88bbdv04e021', null=True, unique=True)),
                ('caller', models.CharField(max_length=150)),
                ('calle', models.CharField(max_length=200)),
                ('start_time', models.TimeField(blank=True)),
                ('end_time', models.TimeField(blank=True)),
                ('time_duration', models.DurationField()),
                ('call_status', models.CharField(choices=[('complete', 'Complete'), ('not_answered', 'Not Answered'), ('rejected', 'Rejected'), ('busy', 'Busy'), ('waiting', 'Waiting'), ('not_completed', 'Not Completed')], max_length=40)),
                ('customer_call', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='customers.customercall')),
            ],
            options={
                'db_table': 'customer_call_participant',
            },
        ),
        migrations.CreateModel(
            name='CustomerAgentShiftsAttendant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, default='mer-y3py5tjtx38l0002o25yw7123m4-2y', null=True, unique=True)),
                ('shift_datetime', models.DateTimeField(auto_now=True)),
                ('customer_agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.customeragent')),
                ('customer_agent_shift', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='customers.customeragentshift')),
            ],
            options={
                'db_table': 'customer_agent_shift_attendant',
            },
        ),
    ]
