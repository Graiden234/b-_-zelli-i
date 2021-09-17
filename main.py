import discord
from discord.ext import commands
Bot = commands.Bot(command_prefix="!mm ")


@Bot.event
async def on_ready():
    print("Ben hazırım")

@Bot.command()
async def animot(msg):
    await msg.send("Ben sayın Animot, daha yeni yazılmaya başlanmış bir botum pek özelliğim yok.")

@Bot.command()
async def bö(msa):
    await msa.send("https://i.pinimg.com/736x/1e/3e/62/1e3e62961cde08c1ee439ea017715583.jpg")
Bot.run("ODg3NzQ0NTIyNTkzOTE4OTc4.YUImgw.hPWtP6fsRsCEFcEniyEh8-YZC7U")
