# Generated by Django 5.2.1 on 2025-07-27 05:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0009_remove_song_cover_image_album_cover_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeaturedAlbum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.IntegerField(default=1, help_text='Position in slider (1 or 2)')),
                ('custom_heading', models.CharField(blank=True, help_text='Leave blank to use album name', max_length=200)),
                ('custom_subheading', models.CharField(blank=True, max_length=200)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='albums.album')),
            ],
            options={
                'ordering': ['position'],
            },
        ),
    ]
