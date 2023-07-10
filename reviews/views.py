from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from . models import Review, Section
from albums.models import Album

def index(request):
  template = loader.get_template("reviews/index.html")
  context = { 
      "reviews": Review.objects.all(),
  }
  return HttpResponse(template.render(context, request))

def detail(request, review_id):
  template = loader.get_template("reviews/detail.html")
  review = Review.objects.get(id=review_id)
  context = { 
      "review": review,
      "album": Album.objects.get(id=review.album_id),
      "sections": Section.objects.filter(review_id=review_id),
  }
  return HttpResponse(template.render(context, request))

def new(request):
    template = loader.get_template("reviews/new.html")
    album_id = request.GET.get('album_id', '')
    album = Album.objects.get(id=album_id)
    context = { 
        "album": album,
    }
    return HttpResponse(template.render(context, request))

