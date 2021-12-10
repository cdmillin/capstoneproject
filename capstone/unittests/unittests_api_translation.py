import unittest
from django.test import TestCase
from capstone import api_translation


class TestBasic(unittest.TestCase):

    def test_universal_api_response_with_location_and_tag_and_returns_locations(self):
        api = api_translation.Api_Translation()
        items = api.universal_api_response("Milwaukee", "eatingout")
        self.assertEqual(items[0][0], "Leon's Frozen Custard")
        self.assertTrue(items[0][1] != "")
        self.assertEqual(items[1][0], "Comet Cafe")
        self.assertTrue(items[1][1] != "")

    def test_universal_api_response_without_location_and_different_tag_and_returns_locations(self):
        api = api_translation.Api_Translation()
        items = api.universal_api_response("Milwaukee", "sightseeing")
        self.assertEqual(items[0][0], "Milwaukee Public Museum")
        self.assertTrue(items[0][1] != "")
        self.assertEqual(items[1][0], "Milwaukee Art Museum")
        self.assertTrue(items[1][1] != "")

    def test_universal_api_response_without_location_and_tag_and_returns_nothing(self):
        api = api_translation.Api_Translation()
        items = api.universal_api_response("", "")
        self.assertEqual(items, [])

    def test_top_cities_in_country_response_with_country_and_returns_cities(self):
        api = api_translation.Api_Translation()
        items = api.top_cities_in_country("France")
        self.assertEqual(items[0][0], "Paris")
        self.assertEqual(items[0][1], "Paris")
        self.assertEqual(items[1][0], "Bordeaux")
        self.assertEqual(items[1][1], "Bordeaux")

    def test_top_cities_in_country_response_with_state_and_returns_cities(self):
        api = api_translation.Api_Translation()
        items = api.top_cities_in_country("Wisconsin")
        self.assertEqual(items[0][0], "Milwaukee")
        self.assertEqual(items[0][1], "Milwaukee")
        self.assertEqual(items[1][0], "Green Bay")
        self.assertEqual(items[1][1], "Green_Bay2C_Wisconsin")

    def test_top_cities_in_country_response_with_nothing_and_returns_nothing(self):
        api = api_translation.Api_Translation()
        items = api.top_cities_in_country("")
        self.assertEqual(items, [])


if __name__ == '__main__':
    unittest.main()