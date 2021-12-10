import requests
from requests.auth import HTTPBasicAuth
auth = {'X-Triposo-Account': 'S5H29H39', 'X-Triposo-Token': 'hg4j9s8dqqu0spgwe32c7h71xykwzngq'}
# hg4j9s8dqqu0spgwe32c7h71xykwzngq = Ben_test api token


class Api_Translation:
    def universal_api_response(self, location, tag_label):
        awaiting_submission = "https://www.triposo.com/api/20211011/poi.json?location_id=" + location + \
                              "&tag_labels=" + tag_label + "&count=2&fields=id,name,score,intro,tag_labels,best_for" \
                              "&order_by=-score"
        # Using headers=auth when calling request sends authentication to avoid 401 error code
        response = requests.get(awaiting_submission, headers=auth)
        response_items = []

        if response.status_code != 200:
            print("Error requesting data from Triposo API: ", response.status_code)
            return response_items

        response_data = response.json()['results']
        for x in response_data:
            response_items.append([x['name'], x['intro']])

        return response_items

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
            cities.append((x['name'], x['id']))

        return cities

if __name__ == 'shopping':
    api = Api_Translation()
    tmp = api.universal_api_response(("paris", "hotels"))
    print(tmp)