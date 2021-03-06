# Generated by Django 4.0.3 on 2022-03-30 23:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0003_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseStudent',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('course', models.ForeignKey(db_column='id_course', on_delete=django.db.models.deletion.DO_NOTHING, to='basic.course')),
            ],
            options={
                'db_table': 'course_student',
                'managed': True,
            },
        ),
        migrations.RemoveField(
            model_name='student',
            name='course',
        ),
        migrations.AddField(
            model_name='student',
            name='courses',
            field=models.ManyToManyField(through='basic.CourseStudent', to='basic.course'),
        ),
        migrations.AddField(
            model_name='coursestudent',
            name='student',
            field=models.ForeignKey(db_column='id_student', on_delete=django.db.models.deletion.DO_NOTHING, to='basic.student'),
        ),
        migrations.AlterUniqueTogether(
            name='coursestudent',
            unique_together={('course', 'student')},
        ),
    ]
