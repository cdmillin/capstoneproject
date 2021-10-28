import requests


class Api_Translation:

    def top_cities_in_country(self, location):
        awaiting_submission = "https://www.triposo.com/api/20211011/location.json?part_of=" + location + "&tag_labels=city&count=10&fields=id,name,score,snippet&order_by=-score"
        response = requests.get(awaiting_submission)
        cities = []

        if response.status_code != 200:
            return cities
        restaurant_data = response.json()['results']
        for x in restaurant_data:
            cities.append(x['id'])

        return cities

    def find_best_resturants(self, location):
        awaiting_submission = "https://www.triposo.com/api/20211011/poi.json?location_id=" + location + "&tag_labels=eatingout&count=10&fields=id,name,score,intro,tag_labels,best_for&order_by=-score"
        response = requests.get(awaiting_submission)
        restaurants = []

        if response.status_code != 200:
            return restaurants

        restaurant_data = response.json()['results']
        for x in restaurant_data:
            restaurants.append(x['name'])

        return restaurants


if __name__ == '__main__':
    api = Api_Translation()
    tmp = api.find_best_resturants("Paris")
    tmp2 = api.top_cities_in_country("France")
    print(tmp2)