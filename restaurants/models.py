from django.db import models

# Create your models here.
#models are for remembering things using database
#creating type of values we need to store in database
class ResturantLocation(models.Model):
    name        = models.CharField(max_length=120)
    location    = models.CharField(max_length=120, null=True, blank=False)
    category    = models.CharField(max_length=120, null=True, blank=True)
    #if auto_now and auto_now_add is true you cant edit tiome in database
    # but its added automatically
    timestamp   = models.DateTimeField(auto_now_add=True)
    updated     = models.DateTimeField(auto_now=True)

    # my_date_field = models.DateField(auto_now_add=False, auto_now=False)




