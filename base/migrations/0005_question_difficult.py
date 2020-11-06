# Generated by Django 3.1.1 on 2020-11-06 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_question_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='difficult',
            field=models.CharField(blank=True, choices=[('E', 'Very Easy'), ('e', 'Easy'), ('m', 'Middle Level'), ('h', 'Hard'), ('H', 'Very Hard')], default='E', max_length=1),
        ),
    ]
