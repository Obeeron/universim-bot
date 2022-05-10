import config
import discord
import minestratorApi
from discord.ext import commands
import periodicTask

bot = commands.Bot(command_prefix='!', case_insensitive=True)

# ==========================
#        BOT EVENTS  
# ==========================

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

    # Add statuc update task
    periodicTask.addPeriodic(config.STATUS_UPDATE_DELAY, update_status)
    
async def update_status():
    serverContents = minestratorApi.getServerContents()
    status = ""
    
    if serverContents == None or serverContents['status'] != 'on':
        status = "Server offline"
    else:
        status = f": {serverContents['players']['online']}/{serverContents['players']['max']}"
    
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(name=status))

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