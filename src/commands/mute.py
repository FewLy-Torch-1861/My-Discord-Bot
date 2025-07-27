from discord import app_commands, Interaction, Member
from datetime import timedelta


def setup_mute_command(bot, GUILD_ID):
    @bot.tree.command(
        name="mute", description="Mute a user in the server", guild=GUILD_ID
    )
    @app_commands.describe(user="The user to mute")
    @app_commands.describe(
        time="Time in seconds to mute the user (default is 5 minutes)"
    )
    async def mute_command(interaction: Interaction, user: Member, time: int = 300):
        if interaction.user.guild_permissions.mute_members:
            await user.timeout(
                timedelta(seconds=time), reason=f"Muted by {interaction.user.name}"
            )
            await interaction.response.send_message(
                f"{user.mention} has been muted for `{time}` seconds.", ephemeral=True
            )

            print(
                f"Mute command used by {interaction.user.name} in guild {interaction.guild.name} ({interaction.guild.id})"
            )
            print(f"Muted {user.name} for {time} seconds")
        else:
            await interaction.response.send_message(
                f"{interaction.user.mention}, You do not have permission to use this command.",
                ephemeral=True,
            )

            print(
                f"Permission denied for mute command by {interaction.user.name} in guild {interaction.guild.name} ({interaction.guild.id})"
            )
