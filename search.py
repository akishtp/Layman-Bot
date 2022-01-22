import os
import requests
import json

api_key = os.environ['API_KEY']


def search_movies(term):
    title = []
    title_small = []
    desc = []
    desc_small = []
    search = []
    rating = []
    rating_small = []
    pic = []
    pic_small = []
    i = 0
    k = 0
    page = 0
    response = requests.get(
        "https://api.themoviedb.org/3/search/movie?api_key=" + api_key +
        "&language=en-US&query=" + term + "&page=1&include_adult=false")
    json_data = json.loads(response.text)
    size = json_data['total_results']
    while i < size:
        try:
            title_small.append(json_data['results'][k]['title'])
        except:
            title_small.append(json_data['results'][k]['name'])
        desc_small.append(json_data['results'][k]['overview'])
        try:
            pic_path = json_data['results'][k]['poster_path']
            pic_small.append("https://image.tmdb.org/t/p/w500" + pic_path)
        except:
            pic_small = "https://www.publicdomainpictures.net/pictures/280000/velka/not-found-image-15383864787lu.jpg"
        rating_small.append(json_data['results'][k]['vote_average'])
        if len(title_small) == 4:
            title.append(title_small)
            desc.append(desc_small)
            pic.append(pic_small)
            rating.append(rating_small)
            title_small = []
            desc_small = []
            pic_small = []
            rating_small = []
        if (i > 0) and (i % 19 == 0):
            page += 1
            k = -1
            print("Page increased")
            response = requests.get(
                "https://api.themoviedb.org/3/search/movie?api_key=" +
                api_key + "&language=en-US&query=" + term + "&page=" +
                str(page) + "&include_adult=false")
            json_data = json.loads(response.text)
        print(k, i)
        k += 1
        i += 1
    title.append(title_small)
    desc.append(desc_small)
    pic.append(pic_small)
    rating.append(rating_small)
    search = [title, desc, pic, rating]
    return search
