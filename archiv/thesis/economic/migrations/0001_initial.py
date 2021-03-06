# Generated by Django 4.0.3 on 2022-03-22 21:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('technology', '0012_delete_economic'),
    ]

    operations = [
        migrations.CreateModel(
            name='Economic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('electricity_fixed_costs_per_year', models.FloatField(null=True)),
                ('electricity_costs_per_kWh', models.FloatField(null=True)),
                ('electricity_feed_in_tariff_chp', models.FloatField(null=True)),
                ('electricity_feed_in_tariff_for_photovoltaic', models.FloatField(null=True)),
                ('gas_fixed_costs_per_year', models.IntegerField(null=True)),
                ('gas_costs_per_kwh', models.IntegerField(null=True)),
                ('battery_costs_perkW_inverter_power', models.FloatField(null=True)),
                ('battery_costs_perkWh_capacity', models.FloatField(null=True)),
                ('battery_costs_for_maintenance_and_operations', models.FloatField(null=True)),
                ('battery_lifetime', models.FloatField(null=True)),
                ('hydrogen_costs_perkw_electrolyseur_power', models.FloatField(null=True)),
                ('hydrogen_costs_perkw_fuel_cellpower', models.FloatField(null=True)),
                ('hydrogen_costsperkWh_hydrogencapacity', models.FloatField(null=True)),
                ('hydrogen_costs_for_maintenance_and_operations', models.FloatField(null=True)),
                ('hydrogen_lifetime', models.FloatField(null=True)),
                ('hydrogen_interest_rate', models.FloatField(null=True)),
                ('tos', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='technology.tos')),
            ],
        ),
    ]
