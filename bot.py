import discord
from discord.ext import commands

client = discord.Client()
token = open("token.txt", "r").read()

@client.event
async def on_ready():
  print(f"We are live as {client.user}")

@client.event
async def on_message(message):
  if "twitch()" == message.content.lower() and 'commands' == str(message.channel):
    await message.channel.send("Go Follow Melkeydev over at https://www.twitch.tv/melkeydev")

  if "test()" == message.content.lower() and 'commands' == str(message.channel):
    await message.channel.send("Test worked you didnt break it yet")

  if "schedule()" == message.content.lower() and 'commands' == str(message.channel):
    await message.channel.send("Melkey streams start on Mondays, Wednesdays, and Fridays at 9PM EST")

  if "project()" == message.content.lower() and 'commands' == str(message.channel):
    await message.channel.send("Melkey is working on a NBA app written in react to search, and compare player stats! You can find it over at https://github.com/Amokstakov/NewNBAApp")

  if "pow()" == message.content.lower() and 'commands' == str(message.channel):
    await message.channel.send("The pow is a sacred technique practice by the ancient tribes of Konoha.")

  if "crash()" == message.content.lower() and 'commands' == str(message.channel):
    await message.channel.send("Nice try I am impossible to crash")

client.run(token)

