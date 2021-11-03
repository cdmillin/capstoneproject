from django.shortcuts import render, redirect
from django.views import View

# Create your views here.
class Home(View):
    def get(self, request):
        #location names are filled with string Destination as a placeholder.
        #replace locationNames with popular destinations received from api.
        #location info is also filled with a placeholder string.

        location1name = "Destination 1"
        location1info = "Information about destination 1 and things to do"

        location2name = "Destination 2"
        location2info = "Information about destination 2 and things to do"

        location3name = "Destination 3"
        location3info = "Information about destination 3 and things to do."

        return render(request, "home.html", {"location1": location1name, "location2": location2name, "location3": location3name, "location1info": location1info, "location2info": location2info, "location3info": location3info})

    def post(self, request):
        pass

class About(View):
    def get(self, request):
        return render(request, 'about.html')