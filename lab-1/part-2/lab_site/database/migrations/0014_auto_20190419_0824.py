# Generated by Django 2.2 on 2019-04-19 08:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0013_record_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='record',
            old_name='context',
            new_name='content',
        ),
    ]
