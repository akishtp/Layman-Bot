import discord

def embed(ctx, title, description, image):
	embed = discord.Embed(title = "Top trending movies", url = "", description="These are the top trending movies right now", color = )
	embed.set_thumbnail(url = image[0])
	for i in range(5):
		embed.add_field(name=title[i], value=description[i], inline=False)
	embed.set_footer(text="Information requested by {}".format(ctx.author.display_name))


