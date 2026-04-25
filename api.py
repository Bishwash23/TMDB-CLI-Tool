import requests
import os, sys
from dotenv import load_dotenv

load_dotenv()

def get_endpoint(type):
    endpoint_map = {
        "playing" : "/movie/now_playing",
        "popular" : "/movie/popular",
        "top" : "/movie/top_rated",
        "upcoming" : "/movie/upcoming"
    }
    base_url = "https://api.themoviedb.org/3"
    return base_url + endpoint_map[type]

def fetch_movies(type):
    api_key = os.getenv("TMDB_API_KEY")
    if not api_key:
        sys.exit("API key not found")
    
    url = get_endpoint(type)
    params = {"api_key": api_key}

    try:
        response = requests.get(url, params=params)
        if response.status_code != 200:
            sys.exit("API error")
        
        data = response.json()
        return data["results"]
    except ConnectionError:
        sys.exit("Network error")
    except TimeoutError:
        sys.exit("Request timed our")
