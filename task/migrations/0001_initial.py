# Generated by Django 5.0 on 2023-12-10 03:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=200)),
                ('priority', models.CharField(choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')], default='low', max_length=10)),
                ('status', models.CharField(choices=[('todo', 'To Do'), ('in progress', 'In Progress'), ('done', 'Done')], default='todo', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Commends',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=200)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user_info')),
                ('task', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='task.task')),
            ],
        ),
    ]