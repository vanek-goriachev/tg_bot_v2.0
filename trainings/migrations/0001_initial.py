# Generated by Django 4.2.2 on 2023-06-18 18:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('chats', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gym',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('chat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chats.chat')),
            ],
        ),
        migrations.CreateModel(
            name='ScheduleLine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weekday', models.IntegerField()),
                ('sport', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('time', models.TimeField()),
                ('chat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chats.chat')),
                ('gym', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trainings.gym')),
            ],
        ),
        migrations.CreateModel(
            name='ScheduleCorrection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correction_type', models.CharField(choices=[('move', 'move'), ('remove', 'remove'), ('add', 'add')], max_length=100)),
                ('old_date', models.DateTimeField(null=True)),
                ('old_time', models.TimeField(null=True)),
                ('new_date', models.DateTimeField(null=True)),
                ('new_time', models.TimeField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('chat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chats.chat')),
                ('new_gym', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='moved_in', to='trainings.gym')),
                ('old_gym', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='moved_from', to='trainings.gym')),
            ],
        ),
    ]
