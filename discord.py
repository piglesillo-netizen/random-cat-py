import discord
import aiohttp
import asyncio

prefix = "test!"

class MyClient(discord.Client):
    async def on_ready(self):
        print('✅ Logged in as', self.user.name, f"({self.user.id})")

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith(prefix + 'cat'):
            async with aiohttp.ClientSession() as session:
                async with session.get('https://aws.random.cat/meow') as response:
                    if response.status == 200:
                        data = await response.json()
                        await message.channel.send(data['file'])
                    else:
                        await message.channel.send("😿 Couldn't fetch a cat right now.")

intents = discord.Intents.default()
client = MyClient(intents=intents)

client.run('YOUR_DISCORD_BOT_TOKEN')