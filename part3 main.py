import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='>', intents=intents)

@bot.event
async def on_ready():
    print("ログインしました！")
    await bot.change_presence(activity=discord.Game(name="1"))

bot.run("MTAyNTY2ODg5Nzg3OTM2NzY5Mg.GMbw0K.0wV8wE0TwuaVqOSFYLx7drgLH7FWA0Rplv8AoY")
