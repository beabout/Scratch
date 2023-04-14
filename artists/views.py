from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from . models import Artist

def index(request):
    template = loader.get_template("artists/index.html")
    context = { 
        "artists": Artist.objects.all(),
    }
    return HttpResponse(template.render(context, request))

def detail(request, artist_id):
  template = loader.get_template("artists/detail.html")
  artist = Artist.objects.get(id=artist_id)
  context = { 
      'artist': artist,
      'albums': artist.album_set.all(),
  }
  return HttpResponse(template.render(context, request))