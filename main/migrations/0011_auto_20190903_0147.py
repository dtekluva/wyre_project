# Generated by Django 2.0 on 2019-09-03 00:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20190903_0145'),
    ]

    operations = [
        migrations.RenameField(
            model_name='device',
            old_name='last_day_energy',
            new_name='previous_day_energy',
        ),
        migrations.RenameField(
            model_name='device',
            old_name='last_day_energy_post_datetime',
            new_name='previous_day_energy_post_datetime',
        ),
    ]