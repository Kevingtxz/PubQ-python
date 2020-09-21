# Generated by Django 3.1.1 on 2020-09-21 03:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_auto_20200921_0006'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('text', models.CharField(max_length=5000)),
                ('standard_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.standarduser')),
            ],
        ),
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('title', models.CharField(max_length=200)),
                ('messages', models.ManyToManyField(to='base.ChatMessage')),
                ('users', models.ManyToManyField(to='base.UserPermission')),
            ],
        ),
    ]