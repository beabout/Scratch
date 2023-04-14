from django.db import models
from reviews.models import Review

class Album(models.Model):
  cover_url = models.CharField(max_length=240)
  spotify_id = models.CharField(max_length=240)
  title = models.CharField(max_length=240)
  release_date = models.DateField()
  total_tracks = models.IntegerField()

  # has many artists via 'self.artists.all()'
  artists = models.ManyToManyField('artists.Artist')

  def tracks(self):
    return Track.objects.filter(album_id=self.id)

  def spotify_url(self):
    return "https://open.spotify.com/album/" + self.spotify_id
  
  def __str__(self):
    return self.title

  def reviews(self):
    return Review.objects.filter(album_id=self.id)

class Track(models.Model):
  title = models.CharField(max_length=240)
  length_in_s = models.IntegerField()
  album = models.ForeignKey(Album, on_delete=models.CASCADE)

  def artists(self):
    return self.album.artists()