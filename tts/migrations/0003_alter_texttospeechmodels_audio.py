# Generated by Django 4.2.2 on 2023-06-15 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tts', '0002_rename_texttospeech_texttospeechmodels'),
    ]

    operations = [
        migrations.AlterField(
            model_name='texttospeechmodels',
            name='audio',
            field=models.FileField(blank=True, upload_to='musics/'),
        ),
    ]
