
# developed by slimmy (slimjimthegrim on discord)

import discord
import json

# Functions

def read_json(file_name):
    try: 
        with open(file_name, 'r') as file:
             data = json.load(file)
             return data
    except FileNotFoundError:
            print(f"Error: File not found: {file_name}")
            return None
    except json.JSONDecodeError:
            print(f"Error: Invalid JSON format in file: {file_name}")
            return

# EXAMPLE Setup
class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

# Import bot info
config = read_json('config.json')
if config == None:
    print(f"Exiting due to invalid config")
    exit()

# Set up bot intents
intents = discord.Intents.default()
intents.message_content = True

# Set up bot client
client = MyClient(intents=intents)
client.run(config["token"])