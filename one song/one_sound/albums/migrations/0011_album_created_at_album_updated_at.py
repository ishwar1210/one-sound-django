# Generated by Django 5.2.1 on 2025-07-27 05:52

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0010_featuredalbum'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='album',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
