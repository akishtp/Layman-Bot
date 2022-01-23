import os
from discord.ext import commands
import json
import requests
from embed import no_results, trending_embed
from embed import search_embed
from embed import movie_embed
from embed import discover_help_embed,help_embed
from embed import discover_embed
from reactions import menu_react
from search import search_movies
from genre import listing_category

bot = commands.Bot(command_prefix="!", help_command=None)
api_key = os.environ['API_KEY']
reactions = ["⬅️", "1⃣", "2⃣", "3⃣", "4⃣", "➡️"]


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
            pic = "https://www.publicdomainpictures.net/pictures/280000/velka/not-found-image-15383864787lu.jpg"
        rating.append(json_data['results'][i]['vote_average'])
    trending = [title, desc, pic, rating]
    return trending


@bot.command(name="hello")
async def hello_world(ctx: commands.Context):
    await ctx.send("Well, hello there!")


@bot.command(name="trending")
async def trending(ctx: commands.Context):
    try:
        movie = trending_movies()
        await ctx.send(
            embed=trending_embed(ctx, movie[0], movie[1], movie[2], movie[3]))
    except:
        await ctx.send("Not Found!")

@bot.command(name="discover")
async def discover(ctx: commands.Context,content_type,genre,sort,order):
      j = 0
      movie = listing_category(content_type,sort,order,genre)
      print(movie[0][j], movie[3][j])
      msg = await ctx.send(embed=discover_embed(ctx, genre, movie[0][j], movie[3][j]))

      await menu_react(msg, len(movie[0][j]), j)
      def check(reaction, user):
          return user == ctx.author and str(reaction.emoji) in reactions

      while True:
          try:
              reaction, user = await bot.wait_for("reaction_add",timeout=25.0,check=check)
              if str(reaction.emoji) == reactions[0]:
                  if j != 0:
                      j -= 1
                      print(j)
                      await msg.edit(
                          embed=discover_embed(ctx, genre, movie[0][j], movie[3][j]))
              elif str(reaction.emoji) == reactions[-1]:
                  j += 1
                  print(j)
                  await msg.edit(
                      embed=discover_embed(ctx, genre, movie[0][j], movie[3][j]))
              elif str(
                      reaction.emoji
              ) == reactions[2] or reactions[3] or reactions[4] or reactions[5]:
                  for i in range(1, 6):
                      if reactions[i] == str(reaction.emoji):
                          await ctx.send(embed=movie_embed(
                              ctx, movie[0][j][i - 1], movie[1][j][i - 1],
                              movie[2][j][i - 1], movie[3][j][i - 1]))
          except:
              print("Timed out")
              break
    
@bot.command(name="help")
async def help(ctx: commands.Context, arg):
    if arg.lower() == "discover":
        await ctx.send(embed=discover_help_embed(ctx))
    elif arg.lower() == "me":
        await ctx.send(embed=help_embed(ctx,bot))


@bot.command(name="invite")
async def create_invite(ctx: commands.Context):
    link = await ctx.channel.create_invite(temporary=False,unique=True,reason=None)
    await ctx.send(link)


@bot.command(name="search")
async def search(ctx: commands.Context, arg):
    j = 0
    movie = search_movies(arg)
    print(movie[0][j], movie[3][j])
    msg = await ctx.send(embed=search_embed(ctx, arg, movie[0][j], movie[3][j]))
    await menu_react(msg, len(movie[0][j]), j)

    def check(reaction, user):
        return user == ctx.author and str(reaction.emoji) in reactions

    while True:
        try:
            reaction, user = await bot.wait_for("reaction_add",timeout=25.0,check=check)
            if str(reaction.emoji) == reactions[0]:
                if j != 0:
                    j -= 1
                    print(j)
                    await msg.edit(
                        embed=search_embed(ctx, arg, movie[0][j], movie[3][j]))
            elif str(reaction.emoji) == reactions[-1]:
                j += 1
                print(j)
                await msg.edit(
                    embed=search_embed(ctx, arg, movie[0][j], movie[3][j]))
            elif str(
                    reaction.emoji
            ) == reactions[2] or reactions[3] or reactions[4] or reactions[5]:
                for i in range(1, 6):
                    if reactions[i] == str(reaction.emoji):
                        await ctx.send(embed=movie_embed(
                            ctx, movie[0][j][i - 1], movie[1][j][i - 1],
                            movie[2][j][i - 1], movie[3][j][i - 1]))
        except:
            print("Timed out")
            break


@bot.command(name="ping")
async def ping(ctx):
    await ctx.send(':ping_pong:\tpong {0}'.format(round(bot.latency, 3)))


token = os.environ['NOT_TOKEN']
bot.run(token)
