from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from . models import Artist
from albums.models import Album

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

def album(request, artist_id, album_id):
  template = loader.get_template("albums/detail.html")
  album = Album.objects.get(id=album_id)
  context = { 
      'album': album,
      'artists': album.artists.all(),
  }
  return HttpResponse(template.render(context, request))