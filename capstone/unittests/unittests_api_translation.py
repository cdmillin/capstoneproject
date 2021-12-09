import unittest
from django.test import TestCase
from capstone import api_translation

class TestBasic(unittest.TestCase):

    def test_universal_api_response_with_location_and_tag_and_returns_locations(self):
        api = Api_Translation()
        items = api.universal_api_response("Milwaukee", "Restaurants")
        self.assertEqual(items, [
            ["Leon's Frozen Custard",
            "Leon's Frozen Custard is a classic family-owned drive-in, specializing in frozen custard, located in Milwaukee, Wisconsin. Opened in 1942, its current appearance as a \"drive-in restaurant\" comes from an early 1950s remodel. It is considered a landmark in the city of Milwaukee. Leon's Frozen Custard claims to be the \"Home of the World's Finest Frozen Custard,\" as noted boldly on its signage. Leon\'s offers the three \"regular\" flavors of vanilla and chocolate and butter pecan. Butter pecan was added on a regular basis because it was so popular. On weekends, \'s adds a fourth flavor."],
            ["Comet Cafe",
            "The most delicious pancake. A nice bar located in the centre that is mentioned often for its excellent hamburgers, home made cupcakes and amazing fries; as well as for fantastic cocktails, good coffee and really good beers. Gluten free menu, rustic interior, hipster waiters and fun atmosphere."]])


    def test_universal_api_response_without_location_and_different_tag_and_returns_locations(self):
        api = Api_Translation()
        items = api.universal_api_response("Milwaukee", "Sightseeing")
        self.assertEqual(items, [
            ["Milwaukee Public Museum",
             "The Milwaukee Public Museum (MPM) is a natural and human history museum in downtown Milwaukee, Wisconsin. The museum was chartered in 1882 and opened to the public in 1884; it is a not-for-profit organization operated by the Milwaukee Public Museum, Inc. MPM has three floors of exhibits and the first Dome Theater in Wisconsin."],
            ["Milwaukee Art Museum"],
            "The Milwaukee Art Museum (MAM) is an art museum in Milwaukee, Wisconsin. Its collection contains nearly 25,000 works of art, making it one of the largest museums in the world."])

    def test_universal_api_response_without_location_and_tag_and_returns_nothing(self):
        api = Api_Translation()
        items = api.universal_api_response("", "")
        self.assertEqual(items, [])

    def test_top_cities_in_country_response_with_country_and_returns_cities(self):
        api = Api_Translation()
        items = api.top_cities_in_country("France")
        self.assertEqual(items, ["Paris", "Bordeaux"])

    def test_top_cities_in_country_response_with_state_and_returns_cities(self):
        api = Api_Translation()
        items = api.top_cities_in_country("Wisconsin")
        self.assertEqual(items, ["Milwaukee", "Green Bay, Wisconsin"])

    def test_top_cities_in_country_response_with_nothing_and_returns_nothing(self):
        api = Api_Translation()
        items = api.top_cities_in_country("")
        self.assertEqual(items, [])
