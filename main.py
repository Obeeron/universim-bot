import requests
import discord
from discord.ext import commands

import yaml

# Load the config file
with open('config.yml', 'r') as ymlfile:
    cfg = yaml.load(ymlfile, Loader=yaml.FullLoader) 

bot = commands.Bot(command_prefix='!', case_insensitive=True)

# ===========================
#      MINESTRATOR API
# ===========================
def getServerContents():
    header = {'Authorization': cfg['minestrator']['api_key'] }
    response = requests.get(f"https://rest.minestrator.com/api/v1/server/content/{cfg['minestrator']['code_support']}", headers=header)
    data = response.json()["data"]
    if data == None:
        return None
    return data[0]

# ==========================
#        BOT EVENTS  
# ==========================

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    # Set the bot's activity to the server ip
    await bot.change_presence(activity=discord.Game(f"{cfg['server']['ip']}"))

# ==========================
#        BOT COMMANDS
# ==========================

@bot.command(name='servinfo', brief = "Get the server's current status")
async def commandServInfo(ctx):
    """ Command: !servinfo
    Send the server's current status to the channel
    Contains the server status, ip, and the number of players
    """
    
    serverContents = getServerContents()
    if(serverContents == None):
        await ctx.send("Could not retrieve server informations.")
        return
    
    status = serverContents['status']
    embed = discord.Embed(title=f"")

    if(status == 'on'):
        embed.color = discord.Color.green()
        maxPlayers = serverContents['players']['max']
        currentPlayers = serverContents['players']['online']
        
        embed.add_field(name="Status", value="🟢 Online", inline=True)
        embed.add_field(name="Players", value=f"► {currentPlayers}/{maxPlayers}", inline=True)
    else:
        embed.color = discord.Color.red()
        embed.add_field(name="Status", value="🔴 Offline", inline=True)
        embed.add_field(name="Players", value="► 0/0", inline=True)
    
    embed.add_field(name="Server IP", value=f"► {cfg['server']['ip']}", inline=False)

    await ctx.send(embed=embed)

if __name__ == '__main__':
    bot.run(cfg['discord']['bot_token'])