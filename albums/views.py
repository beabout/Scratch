from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from . models import Album

def index(request):
    template = loader.get_template("albums/index.html")
    context = { 
        "albums": Album.objects.all(),
    }
    return HttpResponse(template.render(context, request))

def detail(request, album_id):
  template = loader.get_template("albums/detail.html")
  album = Album.objects.get(id=album_id)
  context = { 
      'album': album,
      'artists': album.artists.all(),
  }
  return HttpResponse(template.render(context, request))