# Generated by Django 4.1.5 on 2023-07-01 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tts', '0008_remove_texttospeechmodels_render'),
    ]

    operations = [
        migrations.AddField(
            model_name='texttospeechmodels',
            name='audio_all',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='texttospeechmodels',
            name='audio',
            field=models.URLField(blank=True, max_length=100000, null=True),
        ),
    ]