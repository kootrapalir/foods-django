#to return to html use ..return render()
#render takes 3 arguments, (request, 'templete", {dictionary: "context}
from django.shortcuts import render

#for simple http response right here and now ue this module
from django.http import HttpResponse



#creating views
#function based view
def home(request):

    #for test response
    return HttpResponse("hello")
    # return render(request, "templete", {})