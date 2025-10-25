
# random_cat_bot.py
import discord
from discord.ext import commands
import aiohttp
import asyncio

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.command(name="cat", help="Sends a random cat picture 🐱")
async def cat(ctx):
    async with aiohttp.ClientSession() as session:
        async with session.get("https://aws.random.cat/meow") as response:
            if response.status != 200:
                await ctx.send("😿 Couldn't fetch a cat right now.")
                return
            data = await response.json()
            await ctx.send(data["file"])

# Replace this with your bot token
bot.run("YOUR_DISCORD_BOT_TOKEN_HERE")