import botkey
import discord
from discord.ext import commands, tasks
from datetime import datetime, timedelta
import asyncio

intents = discord.Intents.all()  # enable all intents
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')

    # prune messages every 24 hours
    prune_messages.start()

@tasks.loop(hours=24)
async def prune_messages():
    current_time = datetime.utcnow()
    two_days_ago = current_time - timedelta(days=2)

    target_channel = bot.get_channel(botkey.target_channel_id)
    await target_channel.send('doggy prune messages now :3')

    if target_channel:
        async for message in target_channel.history(limit=None, before=two_days_ago):
            await message.delete()
            await asyncio.sleep(1)
    else:
        print(f"Error: Channel with ID {target_channel_id} not found.")
    await target_channel.send('all done :3')
    
@client.command()
async def servers(ctx):
  servers = list(client.guilds)
  await ctx.send(f"Connected on {str(len(servers))} servers:")
  await ctx.send('\n'.join(guild.name for guild in servers))

bot.run(botkey.key)
