# Generated by Django 5.2.1 on 2025-07-23 17:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_eventdetail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventdetail',
            name='detail_text',
        ),
    ]
