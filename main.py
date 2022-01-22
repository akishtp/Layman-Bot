import os
from discord.ext import commands
import json
import requests
from embed import *
from reactions import *
from search import search_movies

bot = commands.Bot(command_prefix="!")
api_key = os.environ['API_KEY']
reactions = ["⬅️","1⃣", "2⃣", "3⃣", "4⃣", "➡️"]


def trending_movies():
    title = []
    desc = []
    trending = []
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
        try:
          pic_path = json_data['results'][0]['poster_path']
          pic = "https://image.tmdb.org/t/p/w500" + pic_path
        except:
          pic="https://www.publicdomainpictures.net/pictures/280000/velka/not-found-image-15383864787lu.jpg"
        rating.append(json_data['results'][i]['vote_average'])
    trending = [title, desc, pic, rating]
    return trending


@bot.command(name="hello")
async def hello_world(ctx: commands.Context):
    await ctx.send("Hello, world!")


@bot.command(name="trending")
async def trending(ctx: commands.Context):
    try:
      movie = trending_movies()
      await ctx.send(embed=trending_embed(ctx, movie[0], movie[1], movie[2], movie[3]))
    except:
      await ctx.send("Not Found!")


@bot.command(name="search")
async def search(ctx: commands.Context, arg):
    j=0
    movie = search_movies(arg)
    msg = await ctx.send(movie[0][j])
    await menu_react(msg, len(movie[0][j]), j)
    def check(reaction, user):
      return user == ctx.author and str(reaction.emoji) in reactions
    while True:
      reaction, user = await bot.wait_for("reaction_add", timeout=25.0,check=check)
      if str(reaction.emoji) == reactions[0]:
        j-=1
        await msg.edit(content=movie[0][j])
      elif str(reaction.emoji) == reactions[-1]:
        j+=1
        await msg.edit(content=movie[0][j])
      

@bot.command(name="ping")
async def ping(ctx):
    await ctx.send('Pong! {0}'.format(round(bot.latency, 1)))


token = os.environ['NOT_TOKEN']
bot.run(token)
