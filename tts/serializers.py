from rest_framework import serializers

from .models import TextToSpeechModels, SpeechToTextModels


class TextToSpeechSerializers(serializers.ModelSerializer):
    class Meta:
        model = TextToSpeechModels
        fields = '__all__'


class SpeechToTextSerializers(serializers.ModelSerializer):
    class Meta:
        model = SpeechToTextModels
        fields = '__all__'
