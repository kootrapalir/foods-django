from django.contrib import admin

# Register your models here.


#to bring the model into admin page for manipulation
from .models import RestaurantLocation
admin.site.register(RestaurantLocation)


