"""muypicky URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

#to render html without going to views if you dint have any context to sedn
from django.views.generic.base import TemplateView

# from restaurants.views import HomeView


#going to display models values in html page
#also importing many types of queryset made in diff classed
#restaurant_createview for form
from restaurants.views import(
    RestaurantListView,
    RestaurantDetailView,
    restaurant_createview
)

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    #getting home function to default url from browser
    #absolute home url 127.0.0.1:8000
    # .as_view() helps it run like function

    #if you have context run it like this. callign class from view and defining templete name there
    # url(r'^$', HomeView.as_view()),


    url(r'^restaurants/$', RestaurantListView.as_view()),
    #makinglist dynamic with REGX
    #here the slug is transferred to SearchResturantlistview
    # url(r'^restaurants/(?P<slug>\w+)/$', RestaurantListView.as_view()),


    # url that sendds to form page
    url(r'^restaurants/create/$', restaurant_createview),


    #for details when you click in each restaurant
    url(r'^restaurants/(?P<slug>[\w-]+)/$', RestaurantDetailView.as_view()),


    #if you dont have context but only html to send
    #in templete name send html file to render
    url(r'^$', TemplateView.as_view(template_name="home.html")),
    url(r'^about/$', TemplateView.as_view(template_name = "about.html")),
    url(r'^contact/$', TemplateView.as_view(template_name = "contact.html")),
]
