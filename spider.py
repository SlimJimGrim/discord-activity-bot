
import discord

# Class to crawl through discord messages
class DiscordSpider():

    def __init__(self, guild):
        self.guild = guild

    async def test_all_channels(self):
        for channel in self.guild.channels:
            if isinstance(channel, discord.abc.Messageable):
                print(f"\tPrinting message in channel {channel.name}:{channel.id}")
                
                await channel.send('Hello World!')
