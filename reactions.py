reactions = ["⬅️", "1⃣", "2⃣", "3⃣", "4⃣", "➡️"]


async def menu_react(msg, number, pa):
    for i in range(number + 2):
        await msg.add_reaction(reactions[i])
    await msg.add_reaction(reactions[-1])
