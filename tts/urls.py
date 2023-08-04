from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import TextToSpeechAPIView
from .views import SpeechToTextAPIView

urlpatterns = [
    path("tts/", TextToSpeechAPIView.as_view()),
    path("stt/", SpeechToTextAPIView.as_view()),
]
