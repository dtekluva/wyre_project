# Generated by Django 2.0 on 2019-10-31 19:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_auto_20191030_1658'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='thread',
            name='guest',
        ),
        migrations.RemoveField(
            model_name='thread',
            name='host',
        ),
        migrations.RemoveField(
            model_name='message',
            name='thread',
        ),
        migrations.AddField(
            model_name='message',
            name='has_new_message',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='message',
            name='receiver',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='message_reciever', to='main.Customer'),
        ),
        migrations.AddField(
            model_name='message',
            name='sender',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='message_sender', to='main.Customer'),
        ),
        migrations.DeleteModel(
            name='Thread',
        ),
    ]