from django.db import models

# Create your models here.

class MoviewRating(models.Model):
    movieName = models.CharField(max_length=30)
    releaseDate = models.DateField()
    rating = models.IntegerField()