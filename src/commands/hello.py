from discord import Interaction


def setup_hello_command(bot, GUILD_ID):
    @bot.tree.command(
        name="hello", description="Says hello to the user", guild=GUILD_ID
    )
    async def hello_command(interaction: Interaction):
        await interaction.response.send_message(f"Hello, {interaction.user.mention}!")
        print(
            f"Hello command used by {interaction.user.name} in guild {interaction.guild.name} ({interaction.guild.id})"
        )
