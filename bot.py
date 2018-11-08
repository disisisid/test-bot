import os
import discord
from discord.ext import commands

TOKEN = os.getenv('TOKEN')

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
	print('Bot is ready!')

@client.event
async def on_message(message):
	channel = message.channel
	if message.content.startswith('.ping'):
		await client.send_message(channel, 'Pong!')

client.run(TOKEN)

