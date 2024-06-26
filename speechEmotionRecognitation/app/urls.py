from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index , name="home"),
    path('audio/submit', views.audioSubmit , name="audio_submit"),
    path('recording/audio', views.recording , name="recording"),
    path('recording/upload/', views.recordingUpload , name="recording_upload"),
    path('recorded/audio/submit', views.recordedAudioSubmit , name="recorded_audio_submit"),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
