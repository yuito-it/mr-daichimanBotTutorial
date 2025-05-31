import nextcord
from nextcord.ext import commands
import os

intents = nextcord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.event
async def on_command_error(ctx, error):
    embed = nextcord.Embed(title="エラー", color=0xFF0000)
    if isinstance(error, commands.CommandNotFound):
        embed.description = "コマンドが見つかりません。入力を確認してください。"
    elif isinstance(error, commands.MissingRequiredArgument):
        embed.description = "必要な引数が足りません。コマンドの使い方を確認してください。"
    else:
        embed.description = f"エラーが発生しました: {str(error)}"
    await ctx.send(embed=embed)

@bot.command()
async def hello(ctx):
    await ctx.send("こんにちは！")

if __name__ == "__main__":
    bot.run("TOKEN")
