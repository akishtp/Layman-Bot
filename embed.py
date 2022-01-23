import discord
from genre import collect_movie_category
from genre import collect_tv_category


def trending_embed(ctx, title, description, image, rating):
    embed = discord.Embed(
        title="Top trending movies",
        url="",
        description="These are the top trending movies right now",
        color=0xA0DAA9)
    embed.set_thumbnail(url=image)
    for i in range(5):
        embed.add_field(name=title[i] + "\t:star:" + str(rating[i]),
                        value=description[i],
                        inline=False)
        #embed.set_image(url=image)
    embed.set_footer(
        text="Information requested by {}".format(ctx.author.display_name))

    return embed


def movie_embed(ctx, name, description, image, rating):
    embed = discord.Embed(title=name,
                          description=":star:" + str(rating),
                          color=0xD2386C)
    embed.add_field(name="Description", value=description, inline=False)
    embed.set_thumbnail(url=image)
    embed.set_footer(text="requested by {}".format(ctx.author.display_name))
    return embed


arr = [
    "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
    "nine"
]


def search_embed(ctx, arg, title, rating):
    embed = discord.Embed(title="Query results: " + arg,
                          url="",
                          description="Search results",
                          color=0xFCBA03)
    embed.set_author(name=ctx.author.display_name,
                     icon_url=ctx.author.avatar_url)
    for i in range(len(title)):
        embed.add_field(name=":" + arr[i + 1] + ": " + title[i],
                        value=":star:\t" + str(rating[i]),
                        inline=False)
    return embed


def discover_help_embed(ctx):
    movie_category = collect_movie_category()
    tv_category = collect_tv_category()
    embed = discord.Embed(title="Availabe Categories",
                          description="Use this to discover new Movies",
                          color=0xFCBA03)
    embed.set_author(name=ctx.author.display_name,
                     icon_url=ctx.author.avatar_url)
    embed.add_field(name="Type", value="movie, tv", inline=False)
    embed.add_field(name="Genre",
                    value="movie :" + " ".join(movie_category[0]) + "\ntv :" +
                    " ".join(tv_category[0]),
                    inline=False)
    embed.add_field(name="Sort-By",
                    value="popularity, release_date, revenue, title, rating")
    embed.add_field(name="Sort", value="a, d", inline=False)
    return embed


def genre_search(ctx, arg, title, rating):
    embed = discord.Embed(title="Discover new movies",
                          url="",
                          description=arg,
                          color=0xFFFFFF)
    embed.set_author(name=ctx.author.display_name,
                     icon_url=ctx.author.avatar_url)
    for i in range(len(title)):
        embed.add_field(name=":" + arr[i + 1] + ": " + title[i],
                        value=":star:\t" + str(rating[i]),
                        inline=False)
    return embed


def no_results(ctx,arg):
    embed = discord.Embed(title="Query not found", url="", description=arg, color = 0x000000)
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
    return embed


def help_embed(ctx, arg, bot):
    cmds = []
    des = ["Find all commands of the bot","say hello to the bot :wave:","Find what movies are trending eight now!", "discover new movies", "Create an invite link to he channel", "search for a movie", "Play ping pong with the bot"]
    for commands in bot.get_allcommands:
        cmds.append(commands)
    embed = discord.Embed(title="List of commands", url="", description="Bot has " , color= 0xFF5431)
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
    for i in range(len(des)):
        embed.add_field(name=cmd[i], value=des[i], inline=False)
    return embed
    
