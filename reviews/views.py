from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from . models import Review

def index(request):
    template = loader.get_template("reviews/index.html")
    context = { 
        "reviews": Review.objects.all(),
    }
    return HttpResponse(template.render(context, request))

def detail(request, review_id):
  template = loader.get_template("reviews/detail.html")
  context = { 
      "review": Review.objects.get(id=review_id),
  }
  return HttpResponse(template.render(context, request))