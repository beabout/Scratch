from django.db import models
from django.contrib.auth.models import User

class Review(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  album = models.ForeignKey('albums.Album', on_delete=models.CASCADE)
  created_at = models.DateTimeField()
  
  def sections(self):
    return Section.objects.filter(review_id=self.id).order_by('position').values()

  def __str__(self):
    return f'{self.album} ({self.created_at.strftime("%m-%d-%Y")})'

# Reviews have sections, a section could be text, an image or a sound bite
class Section(models.Model):
  position = models.IntegerField()
  text = models.CharField(max_length=1080)
  review = models.ForeignKey(Review, on_delete=models.CASCADE)

  def __str__(self):
    return f'{self.review} #{self.position}'