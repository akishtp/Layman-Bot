import os
from discord.ext import commands
import json
import requests
from embed import *

bot = commands.Bot(command_prefix="!")
api_key = os.environ['API_KEY']


def trending_movies():
    title=[]
    desc=[]
    pic=[]
    trending=[]
    rating = []
    response = requests.get(
        "https://api.themoviedb.org/3/trending/all/day?api_key=" + api_key)
    json_data = json.loads(response.text)
    for i in range(5):
      try:
        title.append(json_data['results'][i]['title'])
      except:
        title.append(json_data['results'][i]['name'])
      desc.append(json_data['results'][i]['overview'])
      pic.append(json_data['results'][i]['poster_path'])
      rating.append(json_data['results'][i]['vote_average'])
    trending = [title, desc, pic, rating]
    return trending


@bot.command(name="hello")
async def hello_world(ctx: commands.Context):
    await ctx.send("Hello, world!")

@bot.command(name="trending")
async def trending(ctx: commands.Context):
    movie = trending_movies()
    await ctx.send(embed=trending_embed(ctx,movie[0],movie[1],movie[2], movie[3]))

@bot.command(name="ping")
async def ping(ctx):
    await ctx.send('Pong! {0}'.format(round(bot.latency, 1)))

token = os.environ['NOT_TOKEN']
bot.run(token)
