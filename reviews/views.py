from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template("reviews/index.html")
    context = { 
        "url": 'https://i.scdn.co/image/ab67616d0000b273cc5c6f9f9d6ca3353dbb6c75',
    }
    return HttpResponse(template.render(context, request))
