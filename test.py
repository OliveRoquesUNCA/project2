from giphy_api import GiphyAPI
import click
import os
import json
import unittest

API_KEY=os.environ["GIPHY_API_KEY"]
class APITest(unittest.TestCase):
    # default small unit test methods compare to searchtest.json and trendingtest.json, 
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
            #print(default_results)
            #testing default trending results
            self.assertEqual(default_results['White Cat Hello GIF'], 'http://gph.is/1kADt78', "key or value incorrect")
            self.assertEqual(len(default_results.keys()), 5, "number of keys != 5")

    #medium unit tests
            
    def test_trending_api_default(self):
        trending_test = GiphyAPI("trending")
        trending_results = trending_test.query()
        self.assertEqual(len(trending_results.keys()), 5, "number of keys != 5")

    def test_trending_api_query(self):
        trending_test = GiphyAPI("trending", limit="2")
        trending_results = trending_test.query()
        self.assertEqual(len(trending_results.keys()), 2, "number of keys != 2")

    def test_search_api_default(self):
        search_test = GiphyAPI("search")
        search_results = search_test.query()
        self.assertEqual(len(search_results.keys()), 5, "number of keys != 5")

    def test_search_api_query(self):
        search_test = GiphyAPI("search", limit="2")
        search_results = search_test.query()
        self.assertEqual(len(search_results.keys()), 2, "number of keys != 2")

#uncomment below if testing
        
#if __name__ == "__main__":
#    unittest.main()

