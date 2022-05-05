import config
import discord
import minestratorApi
from discord.ext import commands


bot = commands.Bot(command_prefix='!', case_insensitive=True)

# ==========================
#        BOT EVENTS  
# ==========================

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    # Set the bot's activity to the server ip
    await bot.change_presence(activity=discord.Game(f"{config.SERVER_IP}"))

# ==========================
#        BOT COMMANDS
# ==========================

@bot.command(name='status', brief = "Get the server's current status")
async def commandStatus(ctx):
    """ Command: !status
    Sends the server's current status to the channel
    Contains the server status, ip, and the number of players
    """
    
    serverContents = minestratorApi.getServerContents()
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
    
    embed.add_field(name="Server IP", value=f"► {config.SERVER_IP}", inline=False)

    await ctx.send(embed=embed)

if __name__ == '__main__':
    # Load the config file
    bot.run(config.BOT_TOKEN)