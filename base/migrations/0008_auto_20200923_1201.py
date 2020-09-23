# Generated by Django 3.1.1 on 2020-09-23 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_auto_20200922_2240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answear',
            name='deslikes',
            field=models.ManyToManyField(blank=True, null=True, to='base.Deslike'),
        ),
        migrations.AlterField(
            model_name='answear',
            name='likes',
            field=models.ManyToManyField(blank=True, null=True, to='base.Like'),
        ),
        migrations.AlterField(
            model_name='answear',
            name='reports',
            field=models.ManyToManyField(blank=True, null=True, to='base.Report'),
        ),
        migrations.AlterField(
            model_name='answear',
            name='text',
            field=models.CharField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='book',
            name='deslikes',
            field=models.ManyToManyField(blank=True, null=True, to='base.Deslike'),
        ),
        migrations.AlterField(
            model_name='book',
            name='likes',
            field=models.ManyToManyField(blank=True, null=True, to='base.Like'),
        ),
        migrations.AlterField(
            model_name='book',
            name='reports',
            field=models.ManyToManyField(blank=True, null=True, to='base.Report'),
        ),
        migrations.AlterField(
            model_name='commentary',
            name='deslike_count',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='commentary',
            name='deslikes',
            field=models.ManyToManyField(blank=True, null=True, to='base.Deslike'),
        ),
        migrations.AlterField(
            model_name='commentary',
            name='like_count',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='commentary',
            name='likes',
            field=models.ManyToManyField(blank=True, null=True, to='base.Like'),
        ),
        migrations.AlterField(
            model_name='commentary',
            name='reports',
            field=models.ManyToManyField(blank=True, null=True, to='base.Report'),
        ),
        migrations.AlterField(
            model_name='question',
            name='answear',
            field=models.CharField(blank=True, max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='answears',
            field=models.ManyToManyField(blank=True, null=True, to='base.Answear'),
        ),
        migrations.AlterField(
            model_name='question',
            name='answears_count',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='question',
            name='commentaries',
            field=models.ManyToManyField(blank=True, null=True, to='base.Commentary'),
        ),
        migrations.AlterField(
            model_name='question',
            name='deslikes',
            field=models.ManyToManyField(blank=True, null=True, to='base.Deslike'),
        ),
        migrations.AlterField(
            model_name='question',
            name='likes',
            field=models.ManyToManyField(blank=True, null=True, to='base.Like'),
        ),
        migrations.AlterField(
            model_name='question',
            name='reports',
            field=models.ManyToManyField(blank=True, null=True, to='base.Report'),
        ),
        migrations.AlterField(
            model_name='university',
            name='commentaries',
            field=models.ManyToManyField(blank=True, null=True, to='base.Commentary'),
        ),
        migrations.AlterField(
            model_name='university',
            name='deslikes',
            field=models.ManyToManyField(blank=True, null=True, to='base.Deslike'),
        ),
        migrations.AlterField(
            model_name='university',
            name='likes',
            field=models.ManyToManyField(blank=True, null=True, to='base.Like'),
        ),
        migrations.AlterField(
            model_name='university',
            name='reports',
            field=models.ManyToManyField(blank=True, null=True, to='base.Report'),
        ),
    ]