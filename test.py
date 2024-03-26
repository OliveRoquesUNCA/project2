import json
import os
import unittest

from giphy_api import GiphyAPI
from giphy_cli import GiphyCLI

API_KEY = os.environ["GIPHY_API_KEY"]


class APITest(unittest.TestCase):
    # default small unit test methods compare to searchtest.json and trendingtest.json,
    # retrieved from GiphyAPI.query_to_file()
    def test_trending_default(self):
        with open("trendingtest.json", "r") as openfile:  # reading from json file
            json_object: dict = json.load(openfile)
            test_default = GiphyAPI("trending")
            default_data: list[dict] = json_object["data"]
            default_results = test_default.get_results(default_data)
            markdown_results = test_default.get_results(default_data, markdown=True)
            print(default_results)
            print(markdown_results)
            # testing default trending results
            self.assertEqual(
                default_results["Lebron James Celebration GIF by EMPIRE"],
                "https://gph.is/g/aQ6866k",
                "key or value incorrect",
            )
            self.assertEqual(len(default_results.keys()), 5, "number of keys != 5")
            self.assertEqual(
                markdown_results["Lebron James Celebration GIF by EMPIRE"],
                "https://media1.giphy.com/media/sBJYYxQvMXxHpMoM6I/giphy.gif?cid=b9130c2eutdlyghobfaxn4it4tudbjku0q5hlh9tg47an9ie&ep=v1_gifs_trending&rid=giphy.gif&ct=g",
                "key or value incorrect",
            )

    def test_search_default(self):
        with open("searchtest.json", "r") as openfile:  # reading from json file
            json_object: dict = json.load(openfile)
            test_default = GiphyAPI("search")
            default_data: list[dict] = json_object["data"]
            default_results = test_default.get_results(default_data)
            markdown_results = test_default.get_results(default_data, markdown=True)
            # print(default_results)
            # testing default trending results
            self.assertEqual(
                default_results["White Cat Hello GIF"],
                "http://gph.is/1kADt78",
                "key or value incorrect",
            )
            self.assertEqual(len(default_results.keys()), 5, "number of keys != 5")
            self.assertEqual(
                markdown_results["White Cat Hello GIF"],
                "https://media2.giphy.com/media/vFKqnCdLPNOKc/giphy.gif?cid=b9130c2e9zwu3hhk37e4rntb7zw7z873gvj4qdmhhyebhqil&ep=v1_gifs_search&rid=giphy.gif&ct=g",
                "key or value incorrect",
            )

    # medium unit tests

    #    def test_trending_api_default(self):
    #        trending_test = GiphyAPI("trending")
    #        trending_results = trending_test.query()
    #        markdown_results = trending_test.query(markdown=True)
    #        self.assertEqual(len(trending_results.items()), 5, "number of keys != 5")
    #        for name, full_url in markdown_results.items():
    #            for title, bitly_url in trending_results.items():
    #                self.assertTrue(len(full_url) > len(bitly_url))

    #def test_trending_cli_default(self):
    #    trending_test = GiphyCLI()
    #    trending_results = trending_test.trending()
    #    markdown_results = trending_test.trending(markdown=True)
    #    self.assertEqual(trending_results.count("\n"), 5, "number of keys != 5")
    #    self.assertTrue(len(markdown_results) > len(trending_results))


#    def test_trending_api_query(self):
#        trending_test = GiphyAPI("trending", limit="2")
#        trending_results = trending_test.query()
#        self.assertEqual(len(trending_results.keys()), 2, "number of keys != 2")

#   def test_search_api_default(self):
#        search_test = GiphyAPI("search")
#        search_results = search_test.query()
#        markdown_results = search_test.query(markdown=True)
#        self.assertEqual(len(search_results.keys()), 5, "number of keys != 5")
#        for name, full_url in markdown_results.items():
#            for title, bitly_url in search_results.items():
#                self.assertTrue(len(full_url) > len(bitly_url))

#    def test_search_api_query(self):
#        search_test = GiphyAPI("search", limit="2")
#        search_results = search_test.query()
#        self.assertEqual(len(search_results.keys()), 2, "number of keys != 2")

# uncomment below if testing

# if __name__ == "__main__":
#    unittest.main()
