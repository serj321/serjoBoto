import discord
import random

TOKEN = "OTY2MDMxOTc2NzY1MjI3MDU4.Yl71Yw.QTfwEulcF-FH1KJRySI_775t9eI"

client = discord.Client()

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    username = str(message.author).split("#")[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f"{username}: {user_message} ({channel})")

    if message.author == client.user:
        return

    if message.channel.name == "general":
        if user_message.lower() == "!random":
            response = f"{random.randint(1, 100)}"
            await message.channel.send(response)
            return
        elif user_message.lower() == "!flip":
            num_to_side = {1: "heads", 2: "tails"}
            await message.channel.send(num_to_side[random.randint(1,2)])
        elif "my friend" in user_message.lower():
            await message.channel.send("MY FRIENDD!!!")

    
    if user_message.lower() == "!anywhere":
        await message.channel.send("This can be used anywhere!")
        return 

client.run(TOKEN)