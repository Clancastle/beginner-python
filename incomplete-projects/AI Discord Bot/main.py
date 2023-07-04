import discord
from discord.ext import commands

token = "MTEyNTU1ODUyMTUxODM3OTE3OA.GcYDAb.OBTW7m2HBfQFR5PT4noYhzJn1P_3nkEwDjtJWk"
link = 'https://discord.com/api/oauth2/authorize?client_id=1125558521518379178&permissions=8&scope=applications.commands%20bot'

bot = commands.Bot(command_prefix='?', intents=discord.Intents.all())
#LEARN -> if long error, copy paste, see what says, then after 10 min no progress, go chatgpt
@bot.event
async def on_ready():
    print('Bot ready.')

@bot.event
async def on_message(message):
    print(f"{message.author.name}: {message}")
    print(message)

bot.run(token)
