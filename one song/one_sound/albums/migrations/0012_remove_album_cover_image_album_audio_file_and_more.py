# Generated by Django 5.2.1 on 2025-07-27 06:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0011_album_created_at_album_updated_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='cover_image',
        ),
        migrations.AddField(
            model_name='album',
            name='audio_file',
            field=models.FileField(blank=True, null=True, upload_to='albums/audio/'),
        ),
        migrations.AlterField(
            model_name='album',
            name='album_image',
            field=models.ImageField(upload_to='albums/'),
        ),
        migrations.AlterField(
            model_name='album',
            name='album_type',
            field=models.CharField(max_length=100),
        ),
        migrations.CreateModel(
            name='NewHit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.PositiveIntegerField(default=1)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='albums.album')),
            ],
        ),
        migrations.CreateModel(
            name='PopularAlbum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.PositiveIntegerField(default=1)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='albums.album')),
            ],
        ),
        migrations.CreateModel(
            name='WeeksTop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.PositiveIntegerField(default=1)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='albums.album')),
            ],
        ),
    ]
