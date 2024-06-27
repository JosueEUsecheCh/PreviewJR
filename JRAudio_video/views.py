from django.shortcuts import render

# Create your views here.
from .models import ComponenteAudioVideo


def audioVideo(request):
    audioVideo = ComponenteAudioVideo.objects.all()
    return render(request, 'audioVideo/audioVideo.html', {'AudioVideo': audioVideo})
