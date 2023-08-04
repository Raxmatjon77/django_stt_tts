from django.db import models


class TextToSpeechModels(models.Model):
    text = models.TextField()
    audio = models.URLField(blank=True, max_length=100000,null=True)
    audio_all=models.TextField(blank=True,null=True)


class SpeechToTextModels(models.Model):
    text=models.TextField(blank=True,null=True)
    audio=models.TextField()


