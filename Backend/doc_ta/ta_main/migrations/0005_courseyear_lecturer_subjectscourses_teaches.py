# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-11 17:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ta_main', '0004_auto_20171111_1222'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseYear',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mandatory_count', models.IntegerField()),
                ('selective_count', models.IntegerField()),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Lecturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=40)),
                ('surname', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='SubjectsCourses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courseyear', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ta_main.CourseYear')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ta_main.Subject')),
            ],
        ),
        migrations.CreateModel(
            name='Teaches',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lecturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ta_main.Lecturer')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ta_main.Subject')),
            ],
        ),
    ]
