from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from playlist.models import Song
from emotions.forms import PredictionForm


@login_required(login_url='accounts:login')
def startpage(request):
    form = PredictionForm()
    return render(request, 'start.html', {'form': form})

