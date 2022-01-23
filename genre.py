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
    categorid=[movie_category,movie_category_id]
    return (categorid)

def listing_category(type,sort,order,genre_id):
    title = []
    title_small = []
    desc = []
    desc_small = []
    rating = []
    rating_small = []
    pic = []
    pic_small = []
    i = 0
    k = 0
    page = 0
    response = requests.get(
        "https://api.themoviedb.org/3/discover/"+type+"?api_key="+api_key+"&language=en-US&sort_by="+sort+"."+order+"&include_adult=false&include_video=false&page=1&with_genres="+genre_id)
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
                "https://api.themoviedb.org/3/discover/"+type+"?api_key="+api_key+"&language=en-US&sort_by="+sort+"."+order+"&include_adult=false&include_video=false&page="+page+"&with_genres="+genre_id)
            json_data = json.loads(response.text)
        print(k, i)
        k += 1
        i += 1
    title.append(title_small)
    desc.append(desc_small)
    pic.append(pic_small)
    rating.append(rating_small)
    movie = [title, desc, pic, rating]
    return movie

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
    categorid=[tv_category,tv_category_id]
    return (categorid)
