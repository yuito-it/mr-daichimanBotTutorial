import discord
from discord.ext import commands



intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print("ボットが起動した！")

@bot.command(pass_content=True)
@commands.has_permissions(administrator=True)
async def nick(ctx, member: discord.Member, nick):
  await member.edit(nick=nick)
  embed = discord.Embed(title="ニックネームを変更しました",description=f"変更された人物: {member.mention}",color=0xffffff)
  await ctx.send(embed=embed)

bot.run("TOKEN")
