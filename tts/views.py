from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
import requests
import json
import time
from gtts import gTTS
from tts.models import TextToSpeechModels, SpeechToTextModels
from config.settings import tts_ai, headers, stt_ai
from tts.serializers import TextToSpeechSerializers, SpeechToTextSerializers
from langdetect import detect
import os


def google_azure_cloud_tts_ai(text):
    payload = {
        "providers": "microsoft",
        "language": "uz-UZ",
        "option": "FEMALE",
        'microsoft': 'uz-UZ-MadinaNeural',
        "text": f"{text}"
    }
    response = requests.post(tts_ai, json=payload, headers=headers)
    result = json.loads(response.text)
    unx_time = int(time.time())

    audio_url = result.get('microsoft').get('audio_resource_url')
    r = requests.get(audio_url)

    with open(f'musics/{unx_time}.wav', 'wb') as file:
        file.write(r.content)

        return audio_url


# def google_cloud_tts_ai(text1):
#     os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./mypjkey.json"
#
#     client = texttospeech.TextToSpeechClient()
#
#     synthesis_input = texttospeech.SynthesisInput(
#         text=text1
#     )
#
#     voice = texttospeech.VoiceSelectionParams(
#         language_code='uz-UZ',
#         name='en-UZ-Wavenet-C',
#         ssml_gender=texttospeech.SsmlVoiceGender.FEMALE)
#
#     audio_config = texttospeech.AudioConfig(
#         audio_encoding=texttospeech.AudioEncoding.MP3)
#
#     response = client.synthesize_speech(
#         input=synthesis_input, voice=voice, audio_config=audio_config
#     )
#
#     # The response's audio_content is binary.
#     with open('musics/output.mp3', 'wb') as out:
#         out.write(response.audio_content)


class TextToSpeechAPIView(APIView):
    def get(self, request):
        tts = TextToSpeechModels.objects.all()
        serializers = TextToSpeechSerializers(tts, many=True)
        return Response(data=serializers.data)

    def post(self, request):
        lang = detect(request.data['text'])

        if lang == "en" or lang == "ru" or lang == "es" or lang == "no" or lang == "hi" or lang == "ja" or lang == "zh" or lang == "af" or lang == "ar" or lang == "bg":

            myObj = gTTS(text=request.data['text'], lang=lang, slow=False)
            unx_time = int(time.time()) + 10
            myObj.save(f"musics/{unx_time}.mp3")
            audio = f"{unx_time}.mp3"
            serializers = TextToSpeechSerializers(
                data={"text": request.data['text'], "audio": 'https://anisaai.uz/api/musics/' + audio})

            serializers.is_valid(raise_exception=True)
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        else:
            text = ""
            for i in request.data['text']:
                if i == "'" or i == "‘" or i == "`":
                    text += "ʻ"
                else:
                    text += i
            audio = google_azure_cloud_tts_ai(text)

            serializers = TextToSpeechSerializers(data={"text": text, "audio": audio
                                                        })

            serializers.is_valid(raise_exception=True)
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)


class SpeechToTextAPIView(APIView):
    def get(self,request):
        stt = SpeechToTextModels.objects.all()
        serializers = SpeechToTextSerializers(stt, many=True)
        return Response(data=serializers.data)

    def post(self, request):
        data = {
            "providers": "neuralspace",
            "language": "uz-UZ",

        }
        print("request.data",request.data)
        
        files = {'file': open(request.data['audio'], 'rb')}
        response = requests.post(stt_ai, data=data, files=files, headers=headers)
        result = json.loads(response.text)
        your_id = result['public_id']
        url1 = f"{stt_ai}/{your_id}"
        while True:
            response1 = requests.get(url1, headers=headers)
            result1 = json.loads(response1.text)
            if result1["status"] == "finished":
                break
        text = str(result1["results"]["neuralspace"]["text"])
        text = text.replace("ʻ", "'")
        text = text.replace("ʼ", "'")
        print
        serializers = SpeechToTextSerializers(data={"text": text, "audio": request.data["audio"]})
        serializers.is_valid(raise_exception=True)
        serializers.save()
        print("serializers.data:" ,serializers.data)
        return Response(serializers.data, status=status.HTTP_201_CREATED)
