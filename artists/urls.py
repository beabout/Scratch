from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:artist_id>/", views.detail, name="detail"),
    path("<int:artist_id>/albums/<int:album_id>", views.album, name="album"),
]
