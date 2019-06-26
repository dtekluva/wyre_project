# Generated by Django 2.0 on 2019-05-14 22:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(blank=True, default=' ', max_length=256, null=True)),
                ('phone', models.CharField(blank=True, default=0, max_length=40, null=True)),
                ('address', models.CharField(blank=True, max_length=40, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='customer', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_id', models.CharField(blank=True, max_length=40, null=True)),
                ('device_type', models.CharField(blank=True, max_length=40, null=True)),
                ('location', models.CharField(blank=True, default=' ', max_length=256, null=True)),
                ('phone', models.CharField(blank=True, default=0, max_length=40, null=True)),
                ('address', models.CharField(blank=True, max_length=40, null=True)),
                ('customer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='device', to='main.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Reading',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_date', models.DateField(auto_now_add=True, verbose_name='date')),
                ('post_time', models.TimeField(blank=True)),
                ('voltage_l1_l12', models.FloatField(blank=True, default=None, null=True)),
                ('voltage_l2_l23', models.FloatField(blank=True, default=None, null=True)),
                ('voltage_l3_l31', models.FloatField(blank=True, default=None, null=True)),
                ('current_l1', models.FloatField(blank=True, default=None, null=True)),
                ('current_l2', models.FloatField(blank=True, default=None, null=True)),
                ('current_l3', models.FloatField(blank=True, default=None, null=True)),
                ('kw_l1', models.FloatField(blank=True, default=None, null=True)),
                ('kw_l2', models.FloatField(blank=True, default=None, null=True)),
                ('kw_l3', models.FloatField(blank=True, default=None, null=True)),
                ('kvar_l1', models.FloatField(blank=True, default=None, null=True)),
                ('kvar_l2', models.FloatField(blank=True, default=None, null=True)),
                ('kvar_l3', models.FloatField(blank=True, default=None, null=True)),
                ('kva_l1', models.FloatField(blank=True, default=None, null=True)),
                ('kva_l2', models.FloatField(blank=True, default=None, null=True)),
                ('kva_l3', models.FloatField(blank=True, default=None, null=True)),
                ('power_factor_l1', models.FloatField(blank=True, default=None, null=True)),
                ('power_factor_l2', models.FloatField(blank=True, default=None, null=True)),
                ('power_factor_l3', models.FloatField(blank=True, default=None, null=True)),
                ('total_kw', models.FloatField(blank=True, default=None, null=True)),
                ('total_kvar', models.FloatField(blank=True, default=None, null=True)),
                ('total_kva', models.FloatField(blank=True, default=None, null=True)),
                ('total_pf', models.FloatField(blank=True, default=None, null=True)),
                ('avg_frequency', models.FloatField(blank=True, default=None, null=True)),
                ('neutral_current', models.FloatField(blank=True, default=None, null=True)),
                ('volt_thd_l1_l12', models.FloatField(blank=True, default=None, null=True)),
                ('volt_thd_l2_l23', models.FloatField(blank=True, default=None, null=True)),
                ('volt_thd_l3_l31', models.FloatField(blank=True, default=None, null=True)),
                ('current_thd_l1', models.FloatField(blank=True, default=None, null=True)),
                ('current_thd_l2', models.FloatField(blank=True, default=None, null=True)),
                ('current_thd_l3', models.FloatField(blank=True, default=None, null=True)),
                ('current_tdd_l1', models.FloatField(blank=True, default=None, null=True)),
                ('current_tdd_l2', models.FloatField(blank=True, default=None, null=True)),
                ('current_tdd_l3', models.FloatField(blank=True, default=None, null=True)),
                ('kwh_import', models.FloatField(blank=True, default=None, null=True)),
                ('kwh_export', models.FloatField(blank=True, default=None, null=True)),
                ('kvarh_import', models.FloatField(blank=True, default=None, null=True)),
                ('kvah_total', models.FloatField(blank=True, default=None, null=True)),
                ('max_amp_demand_l1', models.FloatField(blank=True, default=None, null=True)),
                ('max_amp_demand_l2', models.FloatField(blank=True, default=None, null=True)),
                ('max_amp_demand_l3', models.FloatField(blank=True, default=None, null=True)),
                ('max_sliding_window_kw_demand', models.FloatField(blank=True, default=None, null=True)),
                ('accum_kw_demand', models.FloatField(blank=True, default=None, null=True)),
                ('max_sliding_window_kva_demand', models.FloatField(blank=True, default=None, null=True)),
                ('present_sliding_window_kw_demand', models.FloatField(blank=True, default=None, null=True)),
                ('present_sliding_window_kva_demand', models.FloatField(blank=True, default=None, null=True)),
                ('accum_kva_demand', models.FloatField(blank=True, default=None, null=True)),
                ('pf_import_at_maximum_kva_sliding_window_demand', models.FloatField(blank=True, default=None, null=True)),
            ],
        ),
    ]
