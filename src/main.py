import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

# Import command setup functions
from commands.hello import setup_hello_command
from commands.say import setup_say_command
from commands.ping import setup_ping_command


# Load environment variables from .env file
load_dotenv()
token = os.getenv("DISCORD_TOKEN")

# Set up intents for the bot
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix="!", intents=intents)


# On bot ready event
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name} (ID: {bot.user.id})")

    try:
        guild = discord.Object(id=os.getenv("GUILD_ID"))
        synced = await bot.tree.sync(guild=guild)
        print(f"Synced {len(synced)} commands to the guild {guild.id}")
        print("Commands synced successfully.")
    except Exception as e:
        print(f"Failed to sync commands: {e}")


# Guild ID for faster command registration
GUILD_ID = discord.Object(id=os.getenv("GUILD_ID"))

# Command to say hello to the user (I just added this for testing)
setup_hello_command(bot, GUILD_ID)

# Command to make the bot say something
# Requires the user to have the 'manage_messages' permission
setup_say_command(bot, GUILD_ID)

# Command to check the bot's latency
setup_ping_command(bot, GUILD_ID)


bot.run(token)
