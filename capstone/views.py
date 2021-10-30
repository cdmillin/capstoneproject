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

        # Get the best restaurants in each city and concatenate the city name to the restaurant to make it easy to
        # distinguish in the HTML template. Also capitalize restaurant names because not all come capitalized
        best_restaurants = []
        for city in top_cities_in_country:
            best_restaurants.append([city.replace("2C", ",").replace("_", " ") + "-" + string.capwords(restaurant) for
                                     restaurant in api_translator.find_best_resturants(city)])

        # Use list comprehension to replace 2C with a comma and _ with a space because API outputs some cities like:
        # Niagara_Falls2C_Ontario rather than Niagara Falls, Ontario
        cities = [city.replace("2C", ",").replace("_", " ") for city in top_cities_in_country]

        # Flatten list of restaurants from [[City1-Rest1, City1-Rest2], [City2-Rest1, City2-Rest2]] to
        # [City1-Rest1, City1-Rest2, City2-Rest1, City2-Rest2]
        restaurants = [restaurant for sublist in best_restaurants for restaurant in sublist]

        print(cities)
        print(restaurants)

        return render(request, "home.html", {'location': location, 'cities': cities, 'restaurants': restaurants})

class About(View):
    def get(self, request):
        return render(request, 'about.html')