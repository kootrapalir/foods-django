from django.db import models

# Create your models here.
#models are for remembering things using database
#creating type of values we need to store in database
class ResturantLocation(models.Model):
    name = models.CharField(max_length=120)
    location = models.CharField(max_length=120, null=True, blank=True)


