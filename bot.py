import botkey
import discord
from discord.ext import commands, tasks
from datetime import datetime, timedelta
import asyncio

intents = discord.Intents.all()  # Enable all intents for access to certain events
bot = commands.Bot(command_prefix="!", intents=intents)

  # Replace with the actual channel ID you want to target

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')

    # Start the background task to prune messages every 24 hours
    prune_messages.start()

@tasks.loop(hours=24)
async def prune_messages():
    # Get the current time and calculate the timestamp for 2 days ago
    current_time = datetime.utcnow()
    two_days_ago = current_time - timedelta(days=2)

    # Get the target channel using its ID
    target_channel = bot.get_channel(target_channel_id)
    await target_channel.send('doggy prune messages now :3')

    if target_channel:
        # Fetch messages in chunks and delete those older than 2 days with a delay
        async for message in target_channel.history(limit=None, before=two_days_ago):
            await message.delete()
            await asyncio.sleep(1)  # Add a delay of 1 second to stay within rate limits
    else:
        print(f"Error: Channel with ID {target_channel_id} not found.")
    await target_channel.send('all done :3')

# Run the bot with your token
bot.run(botkey.key)
