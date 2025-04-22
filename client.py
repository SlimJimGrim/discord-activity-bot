
import discord
from spider import DiscordSpider

# Bot client wrapper class
class BotClient(discord.Client):
    
    # Constructor
    def __init__(self, intents, config):
        self.config = config
        super().__init__(intents=intents)
    
    def config(self):
        return self.config

    # Run bot
    def run(self):
        super().run(self.config["token"])
    
    # Run on startup
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

        # Find desired guild
        guild = next(filter(lambda x: x.id == self.config["server_id"], self.guilds), None)
        if guild == None:
            print(f'Error: Cannot find server with id {self.config["server_id"]}')
            await self.close()
            return

        # Create spider
        spider = DiscordSpider(guild=guild)
        print(f"Spider created for guild {guild.name}:{guild.id}")
        await spider.tally_total_messages()

        print(f'All finished!')
        await self.close()

            




