# Generated by Django 2.0 on 2017-02-26 15:47

import compositefk.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gcc_tu_parser', '0003_auto_20170222_1009'),
    ]

    operations = [
        migrations.CreateModel(
            name='FuncParams',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('function_decl', models.IntegerField()),
                ('param_pos', models.IntegerField()),
                ('function_param', models.IntegerField()),
            ],
        ),
    ]
