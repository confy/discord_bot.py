# bot.py
import os
import random
import discord
from discord.ext import commands
from dotenv import load_dotenv



load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
joketxt = open("./Jokebot/jokes.txt", "r")
jokes = joketxt.read()
client = discord.Client()




@client.event
async def on_ready():
    guild = discord.utils.find(lambda g: g.name == GUILD, client.guilds)
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )


client.run(TOKEN)


