# Generated by Django 2.0 on 2019-07-02 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20190702_1716'),
    ]

    operations = [
        migrations.AddField(
            model_name='reading',
            name='post_datetime',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
