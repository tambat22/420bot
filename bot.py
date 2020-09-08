import discord
from discord.ext import commands
import time
from datetime import datetime
import pytz
import asyncio
import os

weedTimeAm = '4:20'
weedTimePm = '16:20'

TOKEN = open("token.txt","r").readline()
client = commands.Bot(command_prefix = '.')

def getTimeRn():
    global datetimern
    global timern
    datetimern = datetime.now(pytz.timezone('US/Pacific'))
    timern = str(datetimern.hour) + ':' + str(datetimern.minute)
    return timern

#WARNING: setting up the bot during any time ending with 59 will cause an infinite loop
def getSetupTime():
    global setupTime
    setupTime = str(datetimern.hour) + ':' + str(datetimern.minute + 1)
    return setupTime

client.remove_command('help')
@client.command()
async def help(ctx):
    embed = discord.Embed(
    color = discord.Color.green(),
    description = 'This bot automatically says "4:20" at 4:20 PST',
    title = ''
    )
    embed.set_author(name='420 Bot', url='https://discord.com/api/oauth2/authorize?client_id=737955537613881384&permissions=271969360&scope=bot', icon_url='https://i.imgur.com/Kgp8PbY.png')
    embed.set_footer(text='Made by: TEIN#0803')
    embed.add_field(name='Commands: ', value='__')
    embed.add_field(name='.isTime', value='Checks if the current time is 4:20', inline=False)
    embed.add_field(name='.say <message>', value='Makes bot say a message', inline=False)
    embed.add_field(name='.sayWide <message>', value='Makes bot say a message, but w i d e', inline=False)
    embed.add_field(name='.ping', value='Returns bot response time in milliseconds', inline=False)
    await ctx.send(embed=embed)

@client.command()
async def ping(ctx):
    await ctx.send(f'Ping: {round (client.latency * 1000)}ms ')

@client.command()
async def sayWide(ctx, *, args):
    await ctx.channel.purge(limit=1)
    text = ''
    for arg in args:
        text += f'{arg} '
    await ctx.send(text)

@client.command()
async def say(ctx, *, msg):
    await ctx.message.delete()
    await ctx.send(msg)

@client.command()
async def isTime(ctx):
    if (timern == weedTimeAm or timern == weedTimePm):
        await ctx.send('Blaze IT Time')
    else:
        await ctx.send('NOT Blaze IT Time')

@client.event
async def on_ready():
    print ('Bot is Online!')

async def constCheck():
    await client.wait_until_ready()
    while client.is_ready():
        if (timern == setupTime):
            print('Bot Timer Initiated')
            while not client.is_closed():
                getTimeRn()
                if (timern == weedTimeAm or timern == weedTimePm):
                    for server in client.guilds:
                            # Spin through every server
                            for channel in server.channels:
                                # Channels on the server
                                if not isinstance(channel, discord.VoiceChannel) and not isinstance(channel, discord.CategoryChannel):
                                    if channel.permissions_for(server.me).send_messages:
                                        await channel.send('4:20 Blaze It')
                                        # So that we don't send to every channel:
                                        break
                                    else:
                                        pass

                    await asyncio.sleep(60)
                else:
                    await asyncio.sleep(60)
        else:
            getTimeRn()
            await asyncio.sleep(1)

print(getTimeRn())
print(getSetupTime())
client.loop.create_task(constCheck())
client.run(TOKEN)
