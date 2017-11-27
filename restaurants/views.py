#to return to html use ..return render()
#render takes 3 arguments, (request, 'templete", {dictionary: "context}



#for simple http response right here and now ue this module
from django.http import HttpResponse



#creating views
#function based view
from django.shortcuts import render


#added for class based view for impoting
from django.views import View

#templete view
from django.views.generic.base import TemplateView

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


def restaurant_listview(request):
    template_name = "restaurants/restaurants_list.html"
    queryset = RestaurantLocation.objects.all()
    context = {
        "object_list": queryset
    }

    return render(request, template_name, context)



