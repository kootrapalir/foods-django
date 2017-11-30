#to return to html use ..return render()
#render takes 3 arguments, (request, 'templete", {dictionary: "context}



#for simple http response right here and now ue this module

from django.http import HttpResponse, HttpResponseRedirect

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
from django.views.generic import ListView, DetailView, CreateView

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


#to use form to take user input
from .forms import RestaurantCreateForm, RestaurantLocationCreateForm

def  restaurant_createview(request):
    #GET and POST according to what method is in you  html form ..default is get
    #with POST with {% csrf_token %} to make it secure
    #the data of form is with request.GET/POST as dictionary file


    #instantate the from method to pass in templete to vreate from usnig variables in form.py
    form = RestaurantLocationCreateForm()
    errors = None
    # if request.method == "GET":
    #     print("get data")
    #     print(request.GET)
    if request.method == "POST":
        #this is taking data from htm lform directly..titally unsafe
        # title = request.POST.get("title")
        # location = request.POST.get("location")
        # category = request.POST.get("category")

        #now using form.py module we verufy and clean the data...SAFE
        form = RestaurantLocationCreateForm(request.POST)

        #def clean_name() is checked in models class
        if form.is_valid():
            form.save()
            # obj = RestaurantLocation.objects.create(
            #     name =  form.cleaned_data.get("name"),
            #     location  = form.cleaned_data.get("location"),
            #     category = form.cleaned_data.get("category")
            # )

            # AFTER save sending to resturants list page
            return HttpResponseRedirect("/restaurants/")

        #if data on form not valid
        if form.errors:
            errors = form.errors

    template_name = ("restaurants/form.html")
    context = {
        "form": form,
        "errors": errors,
    }

    return render(request, template_name, context)





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

    # #to use links to redirect to resturant link
    # def get_object(self, *args, **kwargs):
    #     rest_id = self.kwargs.get("rest_id")
    #
    #     #this gets the obj from our database using pk/id primary key...
    #     obj = get_object_or_404(RestaurantLocation, id=rest_id)  #id or pk
    #     return obj

class RestaurantCreateView(CreateView):
    form_class = RestaurantLocationCreateForm
    template_name = "restaurants/form.html"
    success_url = "/restaurants/"





