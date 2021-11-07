import requests
from requests.auth import HTTPBasicAuth
auth = {'X-Triposo-Account': 'S5H29H39', 'X-Triposo-Token': 'hg4j9s8dqqu0spgwe32c7h71xykwzngq'} # hg4j9s8dqqu0spgwe32c7h71xykwzngq = Ben_test api token

class Api_Translation:

    def top_cities_in_country(self, location):
        awaiting_submission = "https://www.triposo.com/api/20211011/location.json?part_of=" + location + "&tag_labels=city&count=2&fields=id,name,score,snippet&order_by=-score"
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
        print(location)
        awaiting_submission = "https://www.triposo.com/api/20211011/poi.json?location_id=" + location + "&tag_labels=eatingout&count=2&fields=id,name,score,intro,tag_labels,best_for&order_by=-score"
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

    def find_best_hotels(self, location):
        awaiting_submission = "https://www.triposo.com/api/20211011/poi.json?location_id=" + location + "&tag_labels=hotels&count=2&fields=id,name,score,intro,tag_labels,best_for&order_by=-score"
        # Using headers=auth when calling request sends authentication to avoid 401 error code
        response = requests.get(awaiting_submission, headers=auth)
        hotels = []

        if response.status_code != 200:
            print("Error requesting data from Triposo API: ", response.status_code)
            return hotels

        hotels_data = response.json()['results']
        for x in hotels_data:
            hotels.append([x['name'], x['intro']])
        return hotels

    def find_best_sightseeing(self, location):
        awaiting_submission = "https://www.triposo.com/api/20211011/poi.json?location_id=" + location + "&tag_labels=sightseeing&count=2&fields=id,name,score,intro,tag_labels,best_for&order_by=-score"
        # Using headers=auth when calling request sends authentication to avoid 401 error code
        response = requests.get(awaiting_submission, headers=auth)
        sights = []

        if response.status_code != 200:
            print("Error requesting data from Triposo API: ", response.status_code)
            return sights

        sights_data = response.json()['results']
        for x in sights_data:
            sights.append([x['name'], x['intro']])
        return sights

if __name__ == '__main__':
    api = Api_Translation()
    tmp = api.find_best_resturants("Paris")
    tmp2 = api.top_cities_in_country("France")
    print(tmp2)