from django.shortcuts import render, redirect
from django.views import View
from capstone.api_translation import *
import string

api_translator = Api_Translation()
# Create your views here.
class Home(View):
    def get(self, request):
        #location names are filled with string Destination as a placeholder.
        #replace locationNames with popular destinations received from api.
        #location info is also filled with a placeholder string.

        #location1name = "Destination 1"
        #location1info = "Information about destination 1 and things to do"

        #location2name = "Destination 2"
        #location2info = "Information about destination 2 and things to do"

        #location3name = "Destination 3"
        #location3info = "Information about destination 3 and things to do."

        #return render(request, "home.html", {"location1": location1name, "location2": location2name, "location3": location3name, "location1info": location1info, "location2info": location2info, "location3info": location3info})


        return render(request, "home.html")


    def post(self, request):
        if 'citybtn' in request.POST:
            city = request.POST.get('citybtn', "")
            city_formatted = city.replace(",", "2C").replace(" ", "_")

            restaurants = {city: api_translator.find_best_resturants(city_formatted)}
            hotels = {city: api_translator.find_best_hotels(city_formatted)}
            sights = {city: api_translator.find_best_sightseeing(city_formatted)}

            return render(request, "city.html", {'city': city, 'restaurants': restaurants, 'sights': sights, 'hotels': hotels})

        elif 'location' in request.POST:
            location = str(request.POST.get("location", "")).title()

            top_cities_in_country = api_translator.top_cities_in_country(location)

            cities = [city.replace("2C", ",").replace("_", " ") for city in top_cities_in_country]

            return render(request, "home.html", {'location': location, 'cities': cities})

class About(View):
    def get(self, request):
        return render(request, 'about.html')

class City(View):
    def get(self, request):
        return render(request, "city.html")

    def post(self, request):
        if 'citybtn' in request.POST:
            city = request.POST.get('citybtn', "")
            print(city)

        return render(request, "city.html", {'city': city})
