import requests
API_KEY = "dWU1i4ScEWx6H1bKo3wC9RnuuU14S1z4"

def get_url_trending():
    url = "https://api.giphy.com/v1/gifs/trending?api_key=" + API_KEY + "&limit=25&offset=0&rating=g"
    return url

def trending_query():
    result = {}
    r = requests.get(get_url_trending())
    result = r.json()
    print(result)

trending_query()