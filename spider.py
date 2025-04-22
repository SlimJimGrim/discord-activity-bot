
import discord
import datetime

# Class to crawl through discord messages
class DiscordSpider():

    def __init__(self, guild):
        self.guild = guild
        self.user_dict = {}
        self.prev_time = None
        self.curr_time = datetime.datetime.now()

    def __inc_user(self, user_id):
        self.user_dict[user_id] = self.user_dict.get(user_id, 0) + 1

    async def tally_total_messages(self):
        for channel in self.guild.channels:
            if isinstance(channel, discord.abc.Messageable):

                # Go through channel history
                counter = 0
                async for message in channel.history(after=self.prev_time, before=self.curr_time, limit=None):
                    self.__inc_user(message.author.id)
                    counter += 1

                print(f"\t#{channel.name}: {counter} msgs")
            
        print(self.user_dict)
                    
                

