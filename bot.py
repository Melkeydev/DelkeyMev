import discord
from discord.ext import commands

client = discord.Client()
token = open("token.txt", "r").read()

@client.event
async def on_ready():
  print(f"We are live as {client.user}")

@client.event
async def on_message(msg):
  channelName = str(msg.channel)

  if channelName != "commands" or channelName != "bot-construction":
    return

  cmd = msg.content.lower()

  if cmd == "twitch()":
    await msg.channel.send("Go Follow Melkeydev over at https://www.twitch.tv/melkeydev")

  if cmd == "test()":
    await msg.channel.send("Test worked you didnt break it yet")

  if cmd == "schedule()":
    await msg.channel.send("Melkey streams start on Mondays, Wednesdays, and Fridays at 9PM EST")

  if cmd == "project()":
    await msg.channel.send("Melkey is working on a NBA app written in react to search, and compare player stats!")

  if cmd == "pow()":
    await msg.channel.send("The pow is a sacred technique practice by the ancient tribes of Konoha.")

  if cmd == "crash()":
    await msg.channel.send("Nice try I am impossible to crash")
    
  if cmd == "dot()":
    await msg.channel.send("Check out my dotfiles at https://github.com/Amokstakov/NvimConfig")

client.run(token)

