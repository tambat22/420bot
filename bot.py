import discord
import time
from datetime import datetime
import pytz
from discord.ext import commands
import asyncio
import os

token = os.environ['DISCORD_TOKEN']

client = commands.Bot(command_prefix = '.')

datetimern = datetime.now(pytz.timezone('US/Pacific'))
timern = str(datetimern.hour) + ':' + str(datetimern.minute)
#WARNING: setting up the bot during any time ending with 9 will cause an infinite loop
setupTime = str(datetimern.hour) + ':' + str(datetimern.minute + 1)
weedTimeAm = '4:20'
weedTimePm = '16:20'

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
    global datetimern
    global timern
    while client.is_ready():
        if (timern == setupTime):
            print('Bot Timer Initiated')
            while not client.is_closed():
                datetimern = datetime.now(pytz.timezone('US/Pacific'))
                timern = str(datetimern.hour) + ':' + str(datetimern.minute)
                if (timern == weedTimeAm or timern == weedTimePm):
                    #THIS ID BELOW IS FOR A TEST SERVER
                    channel = client.get_channel(446140171713511426)
                    await channel.send('4:20 Blaze It')
                    await asyncio.sleep(60)
                else:
                    await asyncio.sleep(60)
        else:
            datetimern = datetime.now(pytz.timezone('US/Pacific'))
            timern = str(datetimern.hour) + ':' + str(datetimern.minute)
            await asyncio.sleep(1)

print(timern)
print(setupTime)
client.loop.create_task(constCheck())
client.run(token)
