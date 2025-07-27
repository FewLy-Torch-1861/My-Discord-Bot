from discord import Interaction


def setup_ping_command(bot, GUILD_ID):
    @bot.tree.command(
        name="ping", description="Check the bot's latency", guild=GUILD_ID
    )
    async def ping_command(interaction: Interaction):
        latency = round(bot.latency * 1000)
        await interaction.response.send_message(f"Pong! Latency: {latency}ms")

        print(
            f"Ping command used by {interaction.user.name} in guild {interaction.guild.name} ({interaction.guild.id})"
        )
