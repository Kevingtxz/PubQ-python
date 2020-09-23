# Generated by Django 3.1.1 on 2020-09-23 19:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_question_is_public'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='discipline',
            name='reports',
        ),
        migrations.AddField(
            model_name='book',
            name='is_public',
            field=models.BooleanField(blank=True, default=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='complement',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='answear',
            name='deslike_count',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='answear',
            name='like_count',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='commentaries',
            field=models.ManyToManyField(blank=True, null=True, to='base.Commentary'),
        ),
        migrations.AlterField(
            model_name='book',
            name='deslike_count',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='like_count',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='commentary',
            name='deslike_count',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='commentary',
            name='like_count',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='discipline',
            name='subjects',
            field=models.ManyToManyField(blank=True, null=True, to='base.Subject'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='answear',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.answear'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='book',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.book'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='commentaries',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.commentary'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='message',
            field=models.CharField(blank=True, default='Hi, see it', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='notification',
            name='question',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.question'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='report',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.report'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='university',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.university'),
        ),
        migrations.AlterField(
            model_name='question',
            name='answears_count',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='deslike_count',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='is_public',
            field=models.BooleanField(blank=True, default=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='like_count',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='university_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='requisition',
            name='standard_user',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='base.standarduser'),
        ),
        migrations.AlterField(
            model_name='standarduser',
            name='nickname',
            field=models.CharField(blank=True, default=models.CharField(max_length=100), max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='standarduser',
            name='notifications',
            field=models.ManyToManyField(blank=True, null=True, to='base.Notification'),
        ),
        migrations.AlterField(
            model_name='standarduser',
            name='phone',
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name='standarduser',
            name='reports',
            field=models.ManyToManyField(blank=True, null=True, to='base.Report'),
        ),
        migrations.AlterField(
            model_name='standarduser',
            name='sex',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='university',
            name='deslike_count',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='university',
            name='like_count',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='university',
            name='questions',
            field=models.ManyToManyField(blank=True, null=True, to='base.Question'),
        ),
        migrations.AlterField(
            model_name='userpermission',
            name='standard_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='base.standarduser'),
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('teacher_name', models.CharField(max_length=200)),
                ('education_Level', models.CharField(choices=[('M', 'Master'), ('H', 'High School'), ('P', 'Phd'), ('D', 'Degree'), ('T', 'Tecnical'), ('F', 'Fundamental')], max_length=1)),
                ('is_public', models.BooleanField(blank=True, default=True)),
                ('university_name', models.CharField(blank=True, max_length=200, null=True)),
                ('like_count', models.IntegerField(blank=True, default=0, null=True)),
                ('deslike_count', models.IntegerField(blank=True, default=0, null=True)),
                ('right_answears_count', models.IntegerField(blank=True, default=0, null=True)),
                ('wrong_answears_count', models.IntegerField(blank=True, default=0, null=True)),
                ('pic_1', models.ImageField(blank=True, null=True, upload_to='')),
                ('pic_2', models.ImageField(blank=True, null=True, upload_to='')),
                ('pic_3', models.ImageField(blank=True, null=True, upload_to='')),
                ('pic_4', models.ImageField(blank=True, null=True, upload_to='')),
                ('pic_5', models.ImageField(blank=True, null=True, upload_to='')),
                ('commentaries', models.ManyToManyField(blank=True, null=True, to='base.Commentary')),
                ('deslikes', models.ManyToManyField(blank=True, null=True, to='base.Deslike')),
                ('likes', models.ManyToManyField(blank=True, null=True, to='base.Like')),
                ('questions', models.ManyToManyField(blank=True, to='base.Question')),
                ('reports', models.ManyToManyField(blank=True, null=True, to='base.Report')),
                ('subject', models.ManyToManyField(blank=True, null=True, to='base.Subject')),
                ('users', models.ManyToManyField(blank=True, to='base.UserPermission')),
            ],
        ),
    ]