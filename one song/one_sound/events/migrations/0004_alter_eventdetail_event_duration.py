# Generated by Django 5.2.1 on 2025-07-23 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_remove_eventdetail_detail_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventdetail',
            name='event_duration',
            field=models.TextField(),
        ),
    ]
