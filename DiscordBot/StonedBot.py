#!/usr/bin/python3.10
import asyncio
from nextcord import Intents
from random import randrange
from os import getenv as os_getenv

from lib.BotEngine import BotEngine

intents = Intents.default()
intents.members = True
intents.messages = True

stonedbot_token = os_getenv('STONEDBOT_ACCESS_TOKEN')
if not stonedbot_token:
    print("Token not found")
    exit()

client = BotEngine(intents=intents)
client.run(stonedbot_token)
