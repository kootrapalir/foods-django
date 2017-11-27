#to return to html use ..return render()
#render takes 3 arguments, (request, 'templete", {dictionary: "context}



#for simple http response right here and now ue this module

from django.http import HttpResponse



#creating views
#function based view
#get_boj_404 needed for gettig clicked linkand redirecting
from django.shortcuts import render, get_object_or_404


#added for class based view for impoting
from django.views import View

#templete view
from django.views.generic.base import TemplateView

#to use queryset & listview
#detail view..for details of list file
from django.views.generic import ListView, DetailView

#to show values from model

#
# #for test of templete view
#
# class HomeView(TemplateView):
#     template_name = "home.html"
#
#     #predefind function to override GET request
#     def get_context_data(self, *args, **kwargs):
#         #for getting ocntext
#         #all super methond and put fail safe as .get_context_data
#         #define context = {} later with data
#         context = super(HomeView, self).get_context_data(*args, **kwargs)
#
#         bdd = "Vishaka"
#         mdd = "Shyama"
#         cdd = "Krishna"
#         list_ = [bdd, mdd, cdd]
#         context = {"dds": list_}
#
#         return(context)
from restaurants.models import RestaurantLocation

#q lokups for advanced search
from django.db.models import Q



#
# def restaurant_listview(request):
#     template_name = "restaurants/restaurants_list.html"
#     queryset = RestaurantLocation.objects.all()
#     context = {
#         "object_list": queryset
#     }
#
#     return render(request, template_name, context)


#these 3 classes for the list i want to generate
class RestaurantListView(ListView):

    #no neeed to this templete_name variable if you name your templete name is restaurantlocation_list.html..
    #ie. modelname_list...
    # template_name = "restaurants/restaurants_list.html"

    # this fucntion receives the word from url, self.kwargs.get("slug")
    def get_queryset(self):
        slug = self.kwargs.get("slug")

        # if a person has entered a query show according to the query.here by location
        if slug:
            queryset = RestaurantLocation.objects.filter(
                Q(location__iexact=slug) |
                Q(location__icontains=slug)
            )
        else:
            queryset = RestaurantLocation.objects.all()

        return queryset


#to display details of each restaurant
class RestaurantDetailView(DetailView):
    queryset = RestaurantLocation.objects.all()

    def get_context_data(self, *args, **kwargs):
        #context getting data that corresponds to the value "pk" it gets from url in kwargs.
        context = super(RestaurantDetailView, self).get_context_data(*args, **kwargs)
        print(context)
        return context

    #to use links to redirect to resturant link
    def get_object(self, *args, **kwargs):
        rest_id = self.kwargs.get("rest_id")
        obj = get_object_or_404(RestaurantLocation, id=rest_id)  #id or pk
        return obj







