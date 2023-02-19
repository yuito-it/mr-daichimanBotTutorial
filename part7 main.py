import discord
from discord.ext import commands
import asyncio


intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print("ボットが起動した！")



@bot.command()
@commands.has_permissions(administrator=True)
@commands.has_permissions(manage_channels=True)
async def purge(ctx, amount:int):
    if amount > 1000:
        await ctx.send(f"({amount}/1000) 削除する数が多すぎます。1000文字以内に収めてください")
    else:
        count_members = {}
        messages = await ctx.channel.history(limit=amount).flatten()
        for message in messages[1:]:
            if str(message.author) in count_members:
                count_members[str(message.author)] += 1
            else:
                count_members[str(message.author)] = 1
        new_string = []
        deleted_messages = 0
        for author, message_deleted in list(count_members.items()):
            new_string.append(f"**{author}**: {message_deleted}")
            deleted_messages += message_deleted
        final_string = "\n".join(new_string)
        await ctx.channel.purge(limit=amount+1)
        if deleted_messages == 1:
           msg = await ctx.send(f"{deleted_messages} 件のメッセージが削除されました。 \n\n{final_string}")
        elif deleted_messages == 0:
             msg = await ctx.send("メッセージは削除されませんでした。メッセージが\n2 週間以上経過していないことを確認してください。")
        else:
           msg = await ctx.send(f"{deleted_messages} 件のメッセージが削除されました。 \n\n{final_string}")
           await asyncio.sleep(2)
           await msg.delete()

bot.run("TOKEN")
