import os
import discord
from discord.ext import commands

TOKEN = os.getenv('TOKEN')

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
	print('Bot is ready!')

@client.event
async def on_member_join(member):
	role = discord.utils.get(member.server.roles, name='cat')
	await client.add.roles(member, role)

@client.event
async def on_message(message):
	channel = message.channel
	if message.content.startswith('.ping'):
		await client.send_message(channel, 'Pong!')

client.run(TOKEN)

