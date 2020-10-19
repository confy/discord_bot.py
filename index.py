import os
import discord
import random
from utils import default
from utils.data import Bot, HelpFormat
jokes = []
config = default.get("config.json")
with open('jokes.txt') as f:
    jokes = f.readlines()

print("Logging in...")


bot = Bot(
    command_prefix=config.prefix, prefix=config.prefix,
    owner_ids=config.owners, command_attrs=dict(hidden=True),
    help_command=HelpFormat(),
    intents=discord.Intents(  # kwargs found at https://discordpy.readthedocs.io/en/latest/api.html?highlight=intents#discord.Intents
        guilds=True, members=True, messages=True, reactions=True
    )
)
@bot.event
async def on_message(message):
	if message.content == '!joke':
		await message.channel.send(random.choice(jokes))
        
for file in os.listdir("cogs"):
    if file.endswith(".py"):
        name = file[:-3]
        bot.load_extension(f"cogs.{name}")

try:
    bot.run(config.token)
except Exception as e:
    print(f'Error when logging in: {e}')
