# Generated by Django 5.1.4 on 2025-02-08 06:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Master', '0002_alter_tbl_question_master_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='tbl_question',
        ),
    ]
