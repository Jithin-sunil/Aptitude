# Generated by Django 5.1.4 on 2025-02-14 09:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0004_alter_tbl_master_master_proof'),
        ('User', '0004_tbl_feedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_questionhead',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questionhead_date', models.DateField(auto_now_add=True)),
                ('questionhead_status', models.IntegerField(default=0)),
                ('questionhead_code', models.CharField(max_length=40)),
                ('questionhead_level', models.CharField(max_length=40)),
                ('questionhead_subject', models.CharField(max_length=40)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_user')),
            ],
        ),
    ]
