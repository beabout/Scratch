from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from albums.models import Album
from reviews.models import Review, Section

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

def me(request):
    template = loader.get_template("accounts/me.html")
    context = { 
        "me": request.user,
        "albums": Album.objects.all(),
        "reviews": Review.objects.filter(user_id=request.user)
    }
    return HttpResponse(template.render(context, request))

def review(request, review_id):
  review = Review.objects.get(id=review_id)
  template = loader.get_template("reviews/detail.html")
  context = { 
    "review": review,
    "album": Album.objects.get(id=review.album_id),
    "sections": Section.objects.filter(review_id=review_id),
  }
  return HttpResponse(template.render(context, request))