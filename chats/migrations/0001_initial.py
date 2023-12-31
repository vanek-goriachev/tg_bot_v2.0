# Generated by Django 4.2.2 on 2023-06-18 18:01

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat_id', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ChatSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('welcome_meme', models.ImageField(default='', upload_to='')),
                ('auto_poll', models.BooleanField(default=1)),
                ('GPT_question', models.BooleanField(default=1)),
                ('GPT_yes', models.BooleanField(default=1)),
                ('GPT_maybe', models.BooleanField(default=1)),
                ('GPT_no', models.BooleanField(default=1)),
                ('emoji', models.BooleanField(default=1)),
                ('everyone_is_administrator', models.BooleanField(default=0)),
                ('language', models.CharField(default='Русский', max_length=50)),
                ('poll_send_time', models.TimeField(default=datetime.time(7, 0))),
                ('chat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chats.chat')),
            ],
        ),
        migrations.CreateModel(
            name='ChatAdministrator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('chat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chats.chat')),
            ],
        ),
    ]
