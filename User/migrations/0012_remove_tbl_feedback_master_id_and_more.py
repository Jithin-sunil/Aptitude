# Generated by Django 5.1.4 on 2025-02-15 08:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0011_tbl_feedback'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tbl_feedback',
            name='master_id',
        ),
        migrations.RemoveField(
            model_name='tbl_feedback',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='tbl_questionhead',
            name='user_id',
        ),
        migrations.DeleteModel(
            name='tbl_complaints',
        ),
        migrations.DeleteModel(
            name='tbl_feedback',
        ),
        migrations.DeleteModel(
            name='tbl_questionhead',
        ),
    ]
