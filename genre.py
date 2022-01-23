import requests
import json
import os

api_key = os.environ['API_KEY']

def collect_movie_category():
    movie_category = []
    movie_category_id = []
    response = requests.get(
        "https://api.themoviedb.org/3/genre/movie/list?api_key="+api_key+"&language=en-US"
    )
    json_data = json.loads(response.text)
    size=len(json_data['genres'])
    for i in range(size):
        movie_category.append(json_data['genres'][i]['name'])
        movie_category_id.append(json_data['genres'][i]['id'])
    return (movie_category)


def collect_tv_category():
    tv_category = []
    tv_category_id = []
    response = requests.get(
        "https://api.themoviedb.org/3/genre/tv/list?api_key="+api_key+"&language=en-US"
    )
    json_data = json.loads(response.text)
    size=len(json_data['genres'])
    for i in range(size):
        tv_category.append(json_data['genres'][i]['name'])
        tv_category_id.append(json_data['genres'][i]['id'])
    return (tv_category)


print(collect_movie_category())
