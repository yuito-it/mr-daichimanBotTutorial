import discord
from discord.ext import commands




intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
  print('起動.')
  bot.add_view(Roles())
  
class Roles(discord.ui.View):
  def __init__(self):
    super().__init__(timeout = None)
  @discord.ui.button(label = "追加/削除", custom_id = "Role 1", style = discord.ButtonStyle.blurple)
  async def button1(self, button: discord.ui.Button, interaction: discord.Interaction):
    role = 1251885448649768962
    user = interaction.user
    if role in [y.id for y in user.roles]:
      await user.remove_roles(user.guild.get_role(role))
      await interaction.response.send_message("ロールが削除されました。", ephemeral = True)
    else:
      await user.add_roles(user.guild.get_role(role))
      await interaction.response.send_message("ロールが追加されました。", ephemeral = True)

@bot.command()
async def roles(ctx):
  embed = discord.Embed(title = "ロール選択フォーム", description = "ボタンを押してロールを追加/削除します。",color=0xff0000)
  await ctx.send(embed = embed, view = Roles())

bot.run("TOKEN")#TOKENは他人に今日共有しないでね！
