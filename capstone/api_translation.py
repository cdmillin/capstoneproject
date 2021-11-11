import requests
from requests.auth import HTTPBasicAuth
auth = {'X-Triposo-Account': 'S5H29H39', 'X-Triposo-Token': 'hg4j9s8dqqu0spgwe32c7h71xykwzngq'}
# hg4j9s8dqqu0spgwe32c7h71xykwzngq = Ben_test api token

class Api_Translation:

    def top_cities_in_country(self, location):
        awaiting_submission = "https://www.triposo.com/api/20211011/location.json?part_of=" + location + \
                              "&tag_labels=city&count=2&fields=id,name,score,snippet&order_by=-score"
        # Using headers=auth when calling request sends authentication to avoid 401 error code
        response = requests.get(awaiting_submission, headers=auth)
        cities = []

        if response.status_code != 200:
            print("Error requesting data from Triposo API: ", response.status_code)
            return cities

        city_data = response.json()['results']
        for x in city_data:
            cities.append(x['id'])

        return cities

    def find_best_resturants(self, location):
        awaiting_submission = "https://www.triposo.com/api/20211011/poi.json?location_id=" + location + \
                              "&tag_labels=eatingout&count=2&fields=id,name,score,intro,tag_labels,best_for" \
                              "&order_by=-score"
        # Using headers=auth when calling request sends authentication to avoid 401 error code
        response = requests.get(awaiting_submission, headers=auth)
        restaurants = []

        if response.status_code != 200:
            print("Error requesting data from Triposo API: ", response.status_code)
            return restaurants

        restaurant_data = response.json()['results']
        for x in restaurant_data:
            restaurants.append([x['name'], x['intro']])
        return restaurants

    def find_parks_in_city(self, location):
        awaiting_submission = "https://www.triposo.com/api/20211011/poi.json?location_id=" + location + \
                              "&tag_labels=national_parks&count=2&fields=id,name,score,intro,tag_labels,best_for" \
                              "&order_by=-score"
        # Using headers=auth when calling request sends authentication to avoid 401 error code
        response = requests.get(awaiting_submission, headers=auth)
        parks = []

        if response.status_code != 200:
            print("Error requesting data from Triposo API: ", response.status_code)
            return parks

        park_data = response.json()['results']
        for x in park_data:
            parks.append([x['name'], x['intro']])
        return parks

    def find_beaches_in_city(self, location):
        awaiting_submission = "https://www.triposo.com/api/20211011/poi.json?location_id=" + location + \
                              "&tag_labels=national_parks&count=2&fields=id,name,score,intro,tag_labels,best_for" \
                              "&order_by=-score"
        # Using headers=auth when calling request sends authentication to avoid 401 error code
        response = requests.get(awaiting_submission, headers=auth)
        beaches = []

        if response.status_code != 200:
            print("Error requesting data from Triposo API: ", response.status_code)
            return beaches

        beaches_data = response.json()['results']
        for x in beaches_data:
            beaches.append([x['name'], x['intro']])
        return beaches

    def find_sightseeing_in_city(self, location):
        awaiting_submission = "https://www.triposo.com/api/20211011/poi.json?location_id=" + location + \
                              "&tag_labels=national_parks&count=2&fields=id,name,score,intro,tag_labels,best_for" \
                              "&order_by=-score"
        # Using headers=auth when calling request sends authentication to avoid 401 error code
        response = requests.get(awaiting_submission, headers=auth)
        sightseeing = []

        if response.status_code != 200:
            print("Error requesting data from Triposo API: ", response.status_code)
            return sightseeing

        sightseeing_data = response.json()['results']
        for x in sightseeing_data:
            sightseeing.append([x['name'], x['intro']])
        return sightseeing

    def find_shopping_in_city(self, location):
        awaiting_submission = "https://www.triposo.com/api/20211011/poi.json?location_id=" + location + \
                              "&tag_labels=national_parks&count=2&fields=id,name,score,intro,tag_labels,best_for" \
                              "&order_by=-score"
        # Using headers=auth when calling request sends authentication to avoid 401 error code
        response = requests.get(awaiting_submission, headers=auth)
        shopping = []

        if response.status_code != 200:
            print("Error requesting data from Triposo API: ", response.status_code)
            return shopping

        shopping_data = response.json()['results']
        for x in shopping_data:
            shopping.append([x['name'], x['intro']])
        return shopping

    def find_shopping_in_city(self, location):
        awaiting_submission = "https://www.triposo.com/api/20211011/poi.json?location_id=" + location + \
                              "&tag_labels=national_parks&count=2&fields=id,name,score,intro,tag_labels,best_for" \
                              "&order_by=-score"
        # Using headers=auth when calling request sends authentication to avoid 401 error code
        response = requests.get(awaiting_submission, headers=auth)
        shopping = []

        if response.status_code != 200:
            print("Error requesting data from Triposo API: ", response.status_code)
            return shopping

        shopping_data = response.json()['results']
        for x in shopping_data:
            shopping.append([x['name'], x['intro']])
        return shopping

    def find_transport_in_city(self, location):
        awaiting_submission = "https://www.triposo.com/api/20211011/poi.json?location_id=" + location + \
                              "&tag_labels=national_parks&count=2&fields=id,name,score,intro,tag_labels,best_for" \
                              "&order_by=-score"
        # Using headers=auth when calling request sends authentication to avoid 401 error code
        response = requests.get(awaiting_submission, headers=auth)
        transport = []

        if response.status_code != 200:
            print("Error requesting data from Triposo API: ", response.status_code)
            return transport

        transport_data = response.json()['results']
        for x in transport_data:
            transport.append([x['name'], x['intro']])
        return transport

if __name__ == 'shopping':
    api = Api_Translation()
    tmp = api.find_parks_in_city("WI");
    print(tmp)