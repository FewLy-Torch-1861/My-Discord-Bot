import discord
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv
import os


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
    except Exception as e:
        print(f"Failed to sync commands: {e}")


# Guild ID for faster command registration
GUILD_ID = discord.Object(id=os.getenv("GUILD_ID"))


# Command to say hello to the user (I just added this for testing)
@bot.tree.command(name="hello", description="Says hello to the user", guild=GUILD_ID)
async def hello_command(interaction: discord.Interaction):
    await interaction.response.send_message(
        f"Hello, {interaction.user.mention}!", ephemeral=True
    )


# Command to make the bot say something
# Requires the user to have the 'manage_messages' permission
@bot.tree.command(name="say", description="Make the bot say something", guild=GUILD_ID)
@app_commands.describe(message="The message for the bot to say")
async def say_command(interaction: discord.Interaction, message: str):
    if interaction.user.guild_permissions.manage_messages:
        await interaction.response.send_message("Message sent!", ephemeral=True)
        await interaction.channel.send(message)
    else:
        await interaction.response.send_message(
            f"{interaction.user.mention}, You do not have permission to use this command.",
            ephemeral=True,
        )


# Command to check the bot's latency
@bot.tree.command(name="ping", description="Check the bot's latency", guild=GUILD_ID)
async def ping_command(interaction: discord.Interaction):
    latency = round(bot.latency * 1000)
    await interaction.response.send_message(
        f"Pong! Latency: {latency}ms", ephemeral=True
    )


bot.run(token)
