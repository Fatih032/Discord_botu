import discord
from discord.ext import commands
from utils import *
from functions import *
intents = discord.Intents(messages=True, guilds=True, reactions=True, members=True, presences=True)
Bot = commands.Bot(". ", intents=intents)
game = Game()

@Bot.event
async def on_ready():
    print(("Ben hazırım."))

@Bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name="genel")
    await channel.send(f"{member} aramıza katıldı.Hoş geldin {member}")
@Bot.event
async def on_member_remove(member):
    channel = discord.utils.get(member.guild.text_channels, name="genel")
    await channel.send(f"{member} aramızdan ayrıldı.")

@Bot.command()
async def Merhaba(ctx):
    await ctx.send("Merhaba")

@Bot.command(aliases=["game","oyun"])
async def bot(ctx, *args):
    if "zarat" in args:
        await ctx.send(game.zar_at())

@Bot.command()
async def temizle(ctx, amount = 5):
    await ctx.channel.purge(limit=amount)

@Bot.command()
@commands.has_role("Admin")
async def kick(ctx, member: discord.Member, *args):
    await member.kick()



Bot.run(TOKEN)