# Generated by Django 5.1.4 on 2025-02-08 10:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Guest', '0004_alter_tbl_master_master_proof'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_complaints',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complaint_title', models.CharField(max_length=40)),
                ('conplaint_content', models.CharField(max_length=100)),
                ('complaint_replay', models.CharField(max_length=100, null=True)),
                ('complaint_stautus', models.IntegerField(default=0)),
                ('complaint_date', models.DateField(auto_now_add=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_user')),
            ],
        ),
    ]
