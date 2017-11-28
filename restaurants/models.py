from django.db import models

#for for signals
from django.db.models.signals import pre_save, post_save

#with help of post-save and pre_save we generetare slug now
from .utils import unique_slug_generator

# Create your models here.
#models are for remembering things using database
#creating type of values we need to store in database
class RestaurantLocation(models.Model):
    name        = models.CharField(max_length=120)
    location    = models.CharField(max_length=120, null=True, blank=False)
    category    = models.CharField(max_length=120, null=True, blank=True)
    #if auto_now and auto_now_add is true you cant edit tiome in database
    # but its added automatically
    timestamp   = models.DateTimeField(auto_now_add=True)
     updated     = models.DateTimeField(auto_now=True)

    #making slug bull and blank inly here...otherwise create it in start and make it unique=True
    slug        = models.SlugField(null=True, blank=True)

    # my_date_field = models.DateField(auto_now_add=False, auto_now=False)

    def __str__(self):
        return(self.name)

    #with this we can sue object.title now
    @property
    def title(self):
        return self.name


#these 2 functions are for doing this during and after the new object is being saving or save
#but prefer to do it in during save as its safe
#function to do during save
def rl_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

# #not so safe to save after save
# #function to do after save
# def rl_post_save_receiver(sender, instance, created, *args, **kwargs):
#     print("saved")
#     print(instance.timestamp)
#     if not instance.slug:
#         instance.slug = unique_slug_generator(instance)
#         instance.save()
#connectiong these saving functions to save and saving moments
pre_save.connect(rl_pre_save_receiver, sender = RestaurantLocation)
# post_save.connect(rl_post_save_receiver, sender = RestaurantLocation)

