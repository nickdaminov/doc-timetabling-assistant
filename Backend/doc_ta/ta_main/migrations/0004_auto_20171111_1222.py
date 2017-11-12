# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-11 12:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ta_main', '0003_subject_title_asp'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassTerm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ta_main.Subject')),
            ],
        ),
        migrations.CreateModel(
            name='Term',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('number_of_weeks', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='timeslot',
            name='day',
            field=models.CharField(choices=[('M', 'Monday'), ('Tu', 'Tuesday'), ('W', 'Wednesday'), ('Th', 'Thursday'), ('F', 'Friday')], max_length=2),
        ),
        migrations.AddField(
            model_name='classterm',
            name='term',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ta_main.Term'),
        ),
    ]
