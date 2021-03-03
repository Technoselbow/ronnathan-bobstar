import discord
from discord.ext import commands, tasks
import os
import youtube_dl
from pretty_help import PrettyHelp

token = os.environ["TOKEN"]

client = commands.Bot(command_prefix = "j!", help_command=PrettyHelp())


#Import cog

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")
        print(f"{filename} has loaded.")

client.run(token)
