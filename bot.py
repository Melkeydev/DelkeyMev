import discord
from discord.ext import commands

bot = commands.bot(command_prefix = '!')
token = open("token.txt", "r").read()

@bot.event
async def on_ready():
  print(f"We are live as {client.user}")


@bot.command()
async def twitch(ctx):
  ctx.send("Go Follow Melkeydev over at https://www.twitch.tv/melkeydev")

@bot.command()
async def test(ctx):
  ctx.send("Test worked you didnt break it yet")

@bot.command()
async def schedule(ctx):
  ctx.send("Melkey streams start on Mondays, Wednesdays, and Fridays at 9PM EST")

@bot.command()
async def project(ctx):
  ctx.send("Melkey is working on a NBA app written in react to search, and compare player stats!")

@bot.command()
async def pow(ctx):
  ctx.send("The pow is a sacred technique practice by the ancient tribes of Konoha.")

@bot.command()
async def crash(ctx):
  ctx.send("Nice try I am impossible to crash")
  
@bot.command()
async def dot(ctx):
  ctx.send("Check out my dotfiles at https://github.com/Amokstakov/NvimConfig")
  
bot.run(token)
