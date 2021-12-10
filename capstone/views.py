from django.shortcuts import render, redirect
from django.views import View
from capstone.api_translation import *
import string

api_translator = Api_Translation()


def city_clicked(request):
    city = request.POST.get('citybtn', "")
    city = city.split("'")
    name = city[1]
    id = city[3]

    restaurants = {name: api_translator.universal_api_response(id, "eatingout")}
    hotels = {name: api_translator.universal_api_response(id, "hotels")}
    sights = {name: api_translator.universal_api_response(id, "sightseeing")}
    transport = {name: api_translator.universal_api_response(id, "transport")}
    shopping = {name: api_translator.universal_api_response(id, "shopping")}
    beaches = {name: api_translator.universal_api_response(id, "beaches")}
    parks = {name: api_translator.universal_api_response(id, "national_parks")}

    return render(request, "city.html", {'city': name, 'restaurants': restaurants, 'sights': sights,
                                         'hotels': hotels, 'transport': transport, 'shopping': shopping,
                                         'beaches': beaches, 'parks': parks})


class Home(View):
    def get(self, request):
        return render(request, "home.html")

    def post(self, request):

        if 'citybtn' in request.POST:
            return city_clicked(request)

        elif 'location' in request.POST:
            location = str(request.POST.get("location", "")).title()

            cities = api_translator.top_cities_in_country(location)

            return render(request, "location.html", {'location': location, 'cities': cities})


class About(View):
    def get(self, request):
        return render(request, 'about.html')

    # allows the search bar to function while on the about page.
    def post(self, request):

        if 'citybtn' in request.POST:
            return city_clicked(request)

        elif 'location' in request.POST:
            location = str(request.POST.get("location", "")).title()

            cities = api_translator.top_cities_in_country(location)

            return render(request, "location.html", {'location': location, 'cities': cities})


class City(View):
    def get(self, request):
        return render(request, "city.html")

    def post(self, request):
        print("City")

        if 'citybtn' in request.POST:
            city = request.POST.get('citybtn', "")
            city_formatted = city.replace(",", "2C").replace(" ", "_")

        return render(request, "city.html", {'city': city_formatted})


class Location(View):
    def get(self, request):
        return render(request, "location.html")

    def post(self, request):
        if 'citybtn' in request.POST:
            return city_clicked(request)

        elif 'location' in request.POST:
            location = str(request.POST.get("location", "")).title()

            cities = api_translator.top_cities_in_country(location)

            return render(request, "location.html", {'location': location, 'cities': cities})
