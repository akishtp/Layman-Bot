import os
import discord
import json
import requests

client = discord.Client()
api_key = os.environ['API_KEY']


def trending_movies():
    response = requests.get(
        "https://api.themoviedb.org/3/trending/all/day?api_key=" + api_key)
    json_data = json.loads(response.text)
    trending = json_data['results'][0]['original_title']
    return (trending)


@client.event
async def on_ready():
    print('{0.user} is running. Catch him.'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content

    if msg.startswith('$hello'):
        await message.channel.send("Hello")

    if msg.startswith('$trending'):
        movie = trending_movies()
        await message.channel.send(movie)


my_secret = os.environ['NOT_TOKEN']
client.run(my_secret)
