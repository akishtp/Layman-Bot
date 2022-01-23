import discord

def trending_embed(ctx, title, description, image, rating):
	embed = discord.Embed(title = "Top trending movies", url = "", description="These are the top trending movies right now", color = 0xA0DAA9 )
	embed.set_thumbnail(url = image)
	for i in range(5):
		embed.add_field(name=title[i]+"\t:star:"+str(rating[i]), value=description[i], inline=False)
		#embed.set_image(url=image)
	embed.set_footer(text="Information requested by {}".format(ctx.author.display_name))

	return embed


def movie_embed(ctx, name, description, image, rating):
	embed = discord.Embed(title=name, description = ":star:"+str(rating), color = 0xD2386C)
	embed.add_field(name="Description", value=description, inline=False)
	embed.set_thumbnail(url=image)
	embed.set_footer(text="requested by {}".format(ctx.author.display_name))
	return embed

arr=["zero","one","two","three","four","five","six","seven","eight","nine"]
 
def search_embed(ctx, arg, title, rating):
	embed = discord.Embed(title = "Query results: "+arg, url="", description="Search results", color = 0xFCBA03)
	embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
	for i in range(len(title)):
		embed.add_field(name=":"+arr[i+1]+": "+title[i], value = ":star:\t"+str(rating[i]), inline=False)
	return embed

def category_help_embed(ctx,category,id):
	embed = discord.Embed(title="Availabe Categories", description="Use this to discover new Movies", color = 0xFCBA03)
	embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
	for i in range(len(category)):
		embed.add_field(name=category[i],value=id[i],inline=False)
	return embed

def genre_search(ctx, arg, title, rating):
  embed = discord.Embed(title="Discover new movies", url="", description=arg, color = 0xFFFFFF)
  embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
  for i in range(len(title)):
    embed.add_field(name=":"+arr[i+1]+": "+title[i],value = ":star:\t"+str(rating[i]), inline=False)
  return embed

