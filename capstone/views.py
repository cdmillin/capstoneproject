from django.shortcuts import render, redirect
from django.views import View
from capstone.api_translation import *
import string

api_translator = Api_Translation()
# Create your views here.
class Home(View):
    def get(self, request):
        return render(request, "home.html")

    def post(self, request):
        location = request.POST.get("location", "")
        top_cities_in_country = api_translator.top_cities_in_country(location)

        # Create a dictionary (key = city name, value = list of restaurant names) to make it easy to
        # distinguish in the HTML template. Also capitalize restaurant names because not all come capitalized
        #restaurants = {City1Name: [[City1Rest1Name, City1Rest1Description], [City1Rest2Name, City1Rest2Description]],
        #               City2Name: [[City2Rest1Name, City2Rest1Description], [City2Rest2Name, City2Rest2Description]]}
        restaurants = {}
        for city in top_cities_in_country:
            restaurants[city.replace("2C", ",").replace("_", " ")] = api_translator.find_best_resturants(city)

        # Use list comprehension to replace 2C with a comma and _ with a space because API outputs some cities like:
        # Niagara_Falls2C_Ontario rather than Niagara Falls, Ontario
        cities = [city.replace("2C", ",").replace("_", " ") for city in top_cities_in_country]

        print(cities)
        print(restaurants)

        return render(request, "home.html", {'location': location, 'cities': cities, 'restaurants': restaurants})

class About(View):
    def get(self, request):
        return render(request, 'about.html')