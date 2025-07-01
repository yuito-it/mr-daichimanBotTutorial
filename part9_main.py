import discord
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print("ボットが起動した！")

class Button(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None
    @discord.ui.button(label="ボタン1", style=discord.ButtonStyle.grey)
    async def button1(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.send_message("ボタン1が押されました！")
    @discord.ui.button(label="ボタン2", style=discord.ButtonStyle.blurple)
    async def button2(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.send_message("ボタン2が押されました！")
    @discord.ui.button(label="ボタン3", style=discord.ButtonStyle.green)
    async def button3(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.send_message("ボタン3が押されました！")
    @discord.ui.button(label="ボタン4", style=discord.ButtonStyle.red)
    async def button4(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.send_message("ボタン4が押されました！")

@bot.command()
async def button(ctx):
    view = Button()
    await ctx.send(view=view)

bot.run("TOKEN")#TOKENは他人に今日共有しないでね！
