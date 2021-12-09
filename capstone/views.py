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
        if 'citybtn' in request.POST:
            city = request.POST.get('citybtn', "")
            city_formatted = city.replace(",", "2C").replace(" ", "_")

            restaurants = {city: api_translator.universal_api_response(city_formatted, "eatingout")}
            hotels = {city: api_translator.universal_api_response(city_formatted, "hotels")}
            sights = {city: api_translator.universal_api_response(city_formatted, "sightseeing")}
            transport = {city: api_translator.universal_api_response(city_formatted, "transport")}
            shopping = {city: api_translator.universal_api_response(city_formatted, "shopping")}
            beaches = {city: api_translator.universal_api_response(city_formatted, "beaches")}
            parks = {city: api_translator.universal_api_response(city_formatted, "national_parks")}

            return render(request, "city.html", {'city': city, 'restaurants': restaurants, 'sights': sights,
                                                 'hotels': hotels, 'transport': transport, 'shopping': shopping,
                                                 'beaches': beaches, 'parks': parks})

        elif 'location' in request.POST:
            location = str(request.POST.get("location", "")).title()

            top_cities_in_country = api_translator.top_cities_in_country(location)

            cities = [city.replace("2C", ",").replace("_", " ") for city in top_cities_in_country]

            return render(request, "location.html", {'location': location, 'cities': cities})


class About(View):
    def get(self, request):
        return render(request, 'about.html')

    # allows the search bar to function while on the about page.
    def post(self, request):

        if 'citybtn' in request.POST:
            city = request.POST.get('citybtn', "")
            city_formatted = city.replace(",", "2C").replace(" ", "_")

            restaurants = {city: api_translator.universal_api_response(city_formatted, "eatingout")}
            hotels = {city: api_translator.universal_api_response(city_formatted, "hotels")}
            sights = {city: api_translator.universal_api_response(city_formatted, "sightseeing")}
            transport = {city: api_translator.universal_api_response(city_formatted, "transport")}
            shopping = {city: api_translator.universal_api_response(city_formatted, "shopping")}
            beaches = {city: api_translator.universal_api_response(city_formatted, "beaches")}
            parks = {city: api_translator.universal_api_response(city_formatted, "national_parks")}

            return render(request, "city.html", {'city': city, 'restaurants': restaurants, 'sights': sights,
                                                 'hotels': hotels, 'transport': transport, 'shopping': shopping,
                                                 'beaches': beaches, 'parks': parks})

        elif 'location' in request.POST:
            location = str(request.POST.get("location", "")).title()

            top_cities_in_country = api_translator.top_cities_in_country(location)

            cities = [city.replace("2C", ",").replace("_", " ") for city in top_cities_in_country]

            return render(request, "location.html", {'location': location, 'cities': cities})

class City(View):
    def get(self, request):
        return render(request, "city.html")

    def post(self, request):
        if 'citybtn' in request.POST:
            city = request.POST.get('citybtn', "")
            print(city)

        return render(request, "city.html", {'city': city})


class Location(View):
    def get(self, request):
        return render(request, "location.html")

    def post(self, request):
        if 'citybtn' in request.POST:
            city = request.POST.get('citybtn', "")
            city_formatted = city.replace(",", "2C").replace(" ", "_")

            restaurants = {city: api_translator.find_best_resturants(city_formatted)}
            hotels = {city: api_translator.find_best_hotels(city_formatted)}
            sights = {city: api_translator.find_best_sightseeing(city_formatted)}

            return render(request, "city.html",
                          {'city': city, 'restaurants': restaurants, 'sights': sights, 'hotels': hotels})

        elif 'location' in request.POST:
            location = str(request.POST.get("location", "")).title()

            top_cities_in_country = api_translator.top_cities_in_country(location)

            cities = [city.replace("2C", ",").replace("_", " ") for city in top_cities_in_country]

            return render(request, "location.html", {'location': location, 'cities': cities})
