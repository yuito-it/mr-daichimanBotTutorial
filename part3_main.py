import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='>', intents=intents)

@bot.event
async def on_ready():
    print("ログインしました！")
    await bot.change_presence(activity=discord.Game(name="1"))

bot.run("token")
