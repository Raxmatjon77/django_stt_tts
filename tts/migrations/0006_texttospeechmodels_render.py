# Generated by Django 4.2.2 on 2023-06-22 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tts', '0005_alter_texttospeechmodels_audio'),
    ]

    operations = [
        migrations.AddField(
            model_name='texttospeechmodels',
            name='render',
            field=models.CharField(default='MAN', max_length=10),
        ),
    ]
