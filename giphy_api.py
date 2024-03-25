import requests
from requests.exceptions import HTTPError
import json
import os

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

# TODO: 
# parse response codes
# markdown formatting
# lucky random option

class GiphyAPI:
    query_type:str = ""
    query_url:str = ""
    query_params:dict[str, str] = {}

    def __init__(self, query_type:str, **kwargs):
        self.query_type = query_type

        if(query_type == 'trending'):
            self.query_url = TRENDING_URL
            self.query_params = DEFAULT_TRENDING_PARAMS
            for key, value in kwargs.items():
                self.query_params[key] = value

        elif(query_type == 'search'):
            self.query_url = SEARCH_URL
            self.query_params = DEFAULT_SEARCH_PARAMS
            for key, value in kwargs.items():
                self.query_params[key] = value
    
    def query(self):
        try:
            response = requests.get(self.query_url, params=self.query_params)
            response.raise_for_status()
            json_response:dict = response.json()
            data:list[dict] = json_response['data']
            results = self.get_results(data)
            return results
        
        except HTTPError as httpErr:
            print(f"http error: {httpErr}")
        except Exception as err:
            print(f"other error: {err}")

    def query_to_file(self, filename:str):
        try:
            response = requests.get(self.query_url, params=self.query_params)
            response.raise_for_status()
            json_response:dict = response.json()
            if(self.query_type == 'trending'):
                with open(filename, "w") as outfile:
                    json.dump(json_response, outfile)
            elif(self.query_type == 'search'):
                with open(filename, "w") as outfile:
                    json.dump(json_response, outfile)

        except HTTPError as httpErr:
            print(f"http error: {httpErr}")
        except Exception as err:
            print(f"other error: {err}")

    #retrieves bitly urls and titles from dict objects in list param, storing results as a dictionary
    def get_results(self, data:list[dict]):
        results = {}
        for gif in data:
            results[gif['title']] = gif['bitly_url']
        return results

