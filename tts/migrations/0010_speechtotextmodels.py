# Generated by Django 4.2.2 on 2023-07-31 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tts', '0009_texttospeechmodels_audio_all_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpeechToTextModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, null=True)),
                ('audio', models.FileField(upload_to='')),
            ],
        ),
    ]