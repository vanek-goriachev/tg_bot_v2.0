# Generated by Django 4.2.2 on 2023-06-22 22:31

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatadministrator',
            name='chat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chat_administrators', to='chats.chat'),
        ),
        migrations.AlterField(
            model_name='chatsettings',
            name='chat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chat_settings', to='chats.chat'),
        ),
        migrations.AlterField(
            model_name='chatsettings',
            name='poll_send_time',
            field=models.TimeField(default=datetime.time(1, 32, 33, 535009)),
        ),
    ]
