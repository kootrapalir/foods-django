from django.db import models

#for for signals
from django.db.models.signals import pre_save, post_save

#with help of post-save and pre_save we generetare slug now

from .utils import unique_slug_generator

#good way of validation
from .validators import validate_category

# Create your models here.
#models are for remembering things using database
#creating type of values we need to store in database

#for user model for making login
from django.conf import settings
#default user model
#too many thigs with suer model..research more
User = settings.AUTH_USER_MODEL


#url resolver
from django.core.urlresolvers import reverse
class RestaurantLocation(models.Model):
    #adding users for data owning
    owner        = models.ForeignKey(User)
    name        = models.CharField(max_length=120)
    location    = models.CharField(max_length=120, null=True, blank=False)
    category    = models.CharField(max_length=120, null=True, blank=True, validators = [validate_category])
    #if auto_now and auto_now_add is true you cant edit tiome in database
    # but its added automatically
    timestamp   = models.DateTimeField(auto_now_add=True)
    updated     = models.DateTimeField(auto_now=True)

    #making slug bull and blank inly here...otherwise create it in start and make it unique=True
    slug        = models.SlugField(null=True, blank=True)

    # my_date_field = models.DateField(auto_now_add=False, auto_now=False)

    def __str__(self):
        return(self.name)

    #reverse url patter
    def get_absolute_url(self):
        # return f"/restaurants/{self.slug}"#bad way can be useless if url changed in urls.py
        return reverse("restaurants:detail", kwargs={"slug": self.slug})

    #with this we can sue object.title now
    @property
    def title(self):
        return self.name


#these 2 functions are for doing this during and after the new object is being saving or save
#but prefer to do it in during save as its safe
#function to do during save
def rl_pre_save_receiver(sender, instance, *args, **kwargs):

    #validation of data
    instance.category = instance.category.capitalize()
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

