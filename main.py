
# developed by slimmy (slimjimthegrim on discord)
# uwu

import discord
import json
from client import BotClient

# json read function
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

def main():
    # Import bot info
    config = read_json('config.json')
    if config == None:
        print(f"Exiting due to invalid config")
        exit()

    # Set up bot intents
    intents = discord.Intents.default()
    intents.message_content = True

    # Set up bot client
    client = BotClient(intents=intents, config=config)
    client.run()

if __name__ == '__main__':
    main()