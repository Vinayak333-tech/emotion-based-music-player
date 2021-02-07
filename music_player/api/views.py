from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import SongSerializer
from playlist.models import Song

@api_view(['GET'])
def data(request):
    songs=Song.objects.all()
    serializer=SongSerializer(songs,many=True)
    return Response(serializer.data)

@api_view(['PUT'])
def songUpdate(request,pk):
    song=Song.objects.get(id=pk)
    serializer=SongSerializer(instance=song, data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        
    else:
        return Response(serializer.errors)