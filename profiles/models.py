from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.core.mail import send_mail
from django.core.urlresolvers import reverse

from .utlis import code_generator
User = settings.AUTH_USER_MODEL

class ProfileManager(models.Model):
    def toggle_follow(self, request_user, username_to_toggle):
        profile_ = Profile.objects.get(user__username__iexact=username_to_toggle)
        user = request_user
        is_following = False
        if user in profile_.followers.all():
            profile_.followers.remove(user)
        else:
            profile_.followers.add(user)
            is_following = True
        return profile_, is_following



class ProfileManager(models.Manager):
    def toggle_follow(self, request_user, username_to_toggle):
        profile_ = Profile.objects.get(user__username__iexact=username_to_toggle)
        user = request_user
        is_following = False
        if user in profile_.followers.all():
            profile_.followers.remove(user)
        else:
            profile_.followers.add(user)
            is_following = True
        return profile_, is_following

class Profile(models.Model):
    user              = models.OneToOneField(User) # user.profile
    followers         = models.ManyToManyField(User, related_name='is_following', blank=True) # user.is_following.all()
    #following         = models.ManyToManyField(User, related_name='following', blank=True) # user.following.all()
    activation_key      = models.CharField(max_length=120, blank=True, null=True)
    activated         = models.BooleanField(default=False)
    timestamp         = models.DateTimeField(auto_now_add=True)
    updated           = models.DateTimeField(auto_now=True)

    objects = ProfileManager()

    def __str__(self):
        return self.user.username

    def send_activation_email(self):
        if not self.activated:
            self.activation_key = code_generator()
            self.save()
            path_ = reverse('activate', kwargs={"code": self.activation_key})
            send_mail("activate email",
                      f"activate you account here {self.activation_key}",
                      settings.DEFAULT_FROM_EMAIL,
                      [self.user.email])
            sent_mail = False
            return sent_mail



def post_save_user_receiver(sender, instance, created, *args, **kwargs):
    if created:
        profile, is_created = Profile.objects.get_or_create(user=instance)
        default_user_profile = Profile.objects.get_or_create(user__id=6)[0] #user__username=
        default_user_profile.followers.add(instance)
        profile.followers.add(default_user_profile.user)
        profile.followers.add(2)

post_save.connect(post_save_user_receiver, sender=User)