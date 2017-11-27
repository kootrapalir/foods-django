#to return to html use ..return render()
#render takes 3 arguments, (request, 'templete", {dictionary: "context}



#for simple http response right here and now ue this module
from django.http import HttpResponse



#creating views
#function based view
from django.shortcuts import render
#added for class based view for impoting
from django.views import View



def home(request):

    bdd = "Vishaka"
    mdd = "Shyama"
    cdd = "Krishna"
    list_ = [bdd, mdd, cdd]
    context = {"dds": list_}
    return render(request, "home.html", context)

def about(request):

    context = {}
    return render(request, "about.html", context)

def contact(request):

    context = {}
    return render(request, "contact.html", context)


class ContactView(View):

    #this method gets get request and processes it
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, "contact.html", context)

    # #for processing post methind and so on
    # def post(self, request, *args, **kwargs):
    #         context = {}
    #         return render(request, "contact.html", context)
    #
    # def put(self, request, *args, **kwargs):
    #         context = {}
    #         return render(request, "contact.html", context)



