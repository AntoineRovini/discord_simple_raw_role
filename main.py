import discord
from discord.ext import commands
import os
import asyncio

TOKEN = "your Token ID"
BASE_ID = "your channel ID if you wanna have a log channel or something like that, should be a number suite"

bot = commands.Bot(command_prefix="/", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f"{bot.user} Hello")
    channel = bot.get_channel(BASE_ID)
    await channel.send(f"Hello")

async def load_cogs():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            try:
                await bot.load_extension(f"cogs.{filename[:-3]}")
                print(f"🔄 Cog loaded : {filename}")
            except Exception as e:
                print(f"⚠️ Error while loading {filename} : {e}")

async def main():
    async with bot:
        await load_cogs()
        await bot.start(TOKEN)

asyncio.run(main())