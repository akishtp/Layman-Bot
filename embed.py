import discord

def trending_embed(ctx, title, description, image, rating):
	embed = discord.Embed(title = "Top trending movies", url = "", description="These are the top trending movies right now", color = 0xA0DAA9 )
	embed.set_thumbnail(url = image)
	for i in range(5):
		embed.add_field(name=title[i]+"\t:star:"+str(rating[i]), value=description[i], inline=False)
		#embed.set_image(url=image)
	embed.set_footer(text="Information requested by {}".format(ctx.author.display_name))

	return embed

