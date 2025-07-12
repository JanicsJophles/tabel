import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()  # Loads .env file
TOKEN = os.getenv("DISCORD_TOKEN")  # Store your bot token in .env

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

# Load cogs
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    await bot.load_extension("cogs.fun")  # Load the cog

bot.run(TOKEN)
