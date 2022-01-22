import os
from discord.ext import commands
import json
import requests

bot = commands.Bot(command_prefix="!")
api_key = os.environ['API_KEY']


def trending_movies():
    movies=[]
    response = requests.get(
        "https://api.themoviedb.org/3/trending/all/day?api_key=" + api_key)
    json_data = json.loads(response.text)
    for i in range(2):
      trending = json_data['results'][i]['title'or'name']
      movies.append(trending)
    return (movies)


@bot.command(name="hello")
async def hello_world(ctx: commands.Context):
    await ctx.send("Hello, world!")

@bot.command(name="trending")
async def trending(ctx: commands.Context):
    movie = trending_movies()
    await ctx.send(movie)

@bot.command(name="ping")
async def ping(ctx):
    await ctx.send('Pong! {0}'.format(round(bot.latency, 1)))

token = os.environ['NOT_TOKEN']
bot.run(token)
