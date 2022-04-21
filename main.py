import discord
import os
import random
import civScraper

TOKEN = os.getenv("TOKEN")

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



    user_text = user_message.lower()

    if "my friend" in user_text:
        await message.channel.send("MY FRIENDD!!!")

    if user_text.startswith("!"):

        if user_text == "!random":
            response = f"{random.randint(1, 100)}"
            await message.channel.send(response)
            return

        elif user_text == "!flip":
            num_to_side = {1: "heads", 2: "tails"}
            await message.channel.send(num_to_side[random.randint(1,2)])


        elif user_text.startswith("!civ,"):
            civilization = user_text.split(",")[1]
            civ_desc = civScraper.searchCiv(civilization)
            await message.channel.send(civ_desc)
            

    
    if user_text == "!anywhere":
        await message.channel.send("This can be used anywhere!")
        return 

client.run(TOKEN)