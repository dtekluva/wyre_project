# Generated by Django 2.0 on 2019-07-07 17:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0007_auto_20190707_0714'),
    ]

    operations = [
        migrations.AddField(
            model_name='branch',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='branch_user', to=settings.AUTH_USER_MODEL),
        ),
    ]