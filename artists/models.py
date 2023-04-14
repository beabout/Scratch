from django.db import models

class Artist(models.Model):
  # has many albums via 'album_set.all()'
  name = models.CharField(max_length=240)
  image_url = models.CharField(max_length=360)
  birthdate = models.DateField()

  def __str__(self):
    return self.name