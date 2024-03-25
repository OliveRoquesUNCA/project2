from giphy_api import GiphyAPI
import os
import json
import unittest

API_KEY=os.environ["GIPHY_API_KEY"]
TRENDING_URL = "https://api.giphy.com/v1/gifs/trending"
SEARCH_URL = "http://api.giphy.com/v1/gifs/search"

DEFAULT_TRENDING_PARAMS = {
    "api_key": API_KEY,
    "limit": "5"
}
DEFAULT_SEARCH_PARAMS = {
    "q": "cute cat",
    "api_key": API_KEY,
    "limit": "5"
}

class APITest(unittest.TestCase):
    # default test methods compare to searchtest.json and trendingtest.json, 
    # retrieved from GiphyAPI.query_to_file()
    def test_trending_default(self):
        with open('trendingtest.json', 'r') as openfile: #reading from json file
            json_object:dict = json.load(openfile)
            test_default = GiphyAPI('trending')
            default_data:list[dict] = json_object['data']
            default_results = test_default.get_results(default_data)
            #print(default_results)
            #testing default trending results
            self.assertEqual(default_results['Lebron James Celebration GIF by EMPIRE'], 'https://gph.is/g/aQ6866k', "key or value incorrect")
            self.assertEqual(len(default_results.keys()), 5, "number of keys != 5")

    def test_search_default(self):
        with open('searchtest.json', 'r') as openfile: #reading from json file
            json_object:dict = json.load(openfile)
            test_default = GiphyAPI('search')
            default_data:list[dict] = json_object['data']
            default_results = test_default.get_results(default_data)
            print(default_results)
            #testing default trending results
            self.assertEqual(default_results['White Cat Hello GIF'], 'http://gph.is/1kADt78', "key or value incorrect")
            self.assertEqual(len(default_results.keys()), 5, "number of keys != 5")

    def test_trending_api_default(self):
        trending_test = GiphyAPI("trending")
        trending_results = trending_test.query()
        self.assertEqual(len(trending_results.keys()), 5, "number of keys != 5")

    def test_search_api_default(self):
        search_test = GiphyAPI("trending")
        search_results = search_test.query()
        self.assertEqual(len(search_results.keys()), 5, "number of keys != 5")

if __name__ == "__main__":
    unittest.main()

