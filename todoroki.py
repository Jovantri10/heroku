import discord
import os
from discord.ext import commands
import requests
import dotenv

BOT = commands.Bot(command_prefix='!', case_insensitive=True)
TOKEN = os.environ.get("TOTOK")
BOT.remove_command("help")

@BOT.command()
async def ping(ctx):
  ping = bot.latency * 1000
  wew = round(ping)
  await ctx.send("Pong! Latency is {}".format(wew))

BOT.run(TOKEN)
