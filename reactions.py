import discord

reactions = ["⬅️","1⃣", "2⃣", "3⃣", "4⃣", "➡️"]

def menu_react(ctx, number, msg, pa):
	if pa == 0:
		for i in range(1,number-1):
			ctx.add_reaction(msg, reactions[i])
		i+=1
	else:
		for i in range(number-1):
			ctx.add_reaction(msg, reactions[i])
		i+=1
	ctx.add_reaction(msg, reactions[-1])


