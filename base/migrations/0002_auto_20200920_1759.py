# Generated by Django 3.1.1 on 2020-09-20 20:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='standarduser',
            old_name='address',
            new_name='addresses',
        ),
        migrations.RenameField(
            model_name='university',
            old_name='address',
            new_name='addresses',
        ),
    ]
