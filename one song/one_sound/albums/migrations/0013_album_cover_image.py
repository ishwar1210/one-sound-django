# Generated by Django 5.2.1 on 2025-07-27 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0012_remove_album_cover_image_album_audio_file_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='cover_image',
            field=models.ImageField(blank=True, null=True, upload_to='cover_images/'),
        ),
    ]
