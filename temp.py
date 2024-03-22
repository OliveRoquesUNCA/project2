import requests
import os

API_KEY=os.environ["GIPHY_API_KEY"]

def get_url_trending():
    url = "https://api.giphy.com/v1/gifs/trending?api_key=" + API_KEY + "&limit=25&offset=0&rating=g"
    return url

def trending_query():
    result = {}
    r = requests.get(get_url_trending())
    result = r.json()
    print(result)

trending_query()