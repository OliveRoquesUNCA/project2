import requests
from requests.exceptions import HTTPError
import json
import os

API_KEY=os.environ["GIPHY_API_KEY"]
TRENDING_URL = "https://api.giphy.com/v1/gifs/trending"
SEARCH_URL = "http://api.giphy.com/v1/gifs/search"

TRENDING_PARAMS = {
    "api_key": API_KEY,
    "limit": "5"
}
SEARCH_PARAMS = {
    "api_key": API_KEY,
    "q": "cute cat",
    "limit": "5"
}

class GiphyAPI:
    query_type:str = ""
    query_url:str = ""
    query_params:dict[str, str] = {}

    def __init__(self, query_type:str):
        self.query_type = query_type

        if(query_type == "trending"):
            self.query_url = TRENDING_URL
            self.query_params = TRENDING_PARAMS

        elif(query_type == "search"):
            self.query_url = SEARCH_URL
            self.query_params = SEARCH_PARAMS
    
    #def update_params(self, q, limit, ...):

    def trending_query(self):
        try:
            response = requests.get(self.query_url, params=self.query_params)
            response.raise_for_status()
            #get json
            jsonResponse:dict = response.json()
            data:list[dict] = jsonResponse["data"]
            print("print each url returned")
            urls = self.get_trending_urls(data)
            print(urls)
        
        except HTTPError as http_err:
            print("http error")
        except Exception as err:
            print("other error")

    def get_trending_urls(self, data:list[dict]):
        urls = []
        for gif in data:
            urls.append(gif['bitly_gif_url'])
        return urls
        
        
giphy = GiphyAPI("trending")
giphy.trending_query()
