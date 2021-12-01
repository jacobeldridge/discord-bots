# bot.py
import os
import time
import discord
from discord import channel
from dotenv import load_dotenv
from mcstatus import MinecraftServer
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
server = MinecraftServer("localhost",25565)

client = discord.Client()

@client.event

async def on_ready():
    channel = client.get_channel(id=915384240558981151)
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )
    lagonlinenum = 0
    while True:
        
        query = server.query()
        online = query.players.names
        onlinenum = len(query.players.names)
        if onlinenum != lagonlinenum:
            if onlinenum == 0:
                await channel.send(f"============================================\n**THEY ALL LEFT**\n===================================================")
            else:
                await channel.send(f"THEY ONLINE: **{', '.join(query.players.names)}**")
            lagonlinenum = onlinenum
        else:
            pass
        
        time.sleep(15)


client.run(TOKEN)
# If you know the host and port, you may skip this and use MinecraftServer("example.org", 1234)




# print(f"The server has the following players online: {', '.join(query.players.names)}")