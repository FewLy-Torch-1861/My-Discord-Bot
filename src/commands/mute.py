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
        # Check if the command user has permission to mute members
        if interaction.user.guild_permissions.mute_members:

            # Check if the target user is already muted
            if user.is_timed_out():
                await interaction.response.send_message(
                    f"{user.mention} is already muted.", ephemeral=True
                )
                return

            # Validate the time argument
            if time < 0:
                await interaction.response.send_message(
                    "Time must be a positive integer.", ephemeral=True
                )
                return
            elif time == 0:
                time = 300  # Default mute time is 5 minutes

                await interaction.response.send_message(
                    f"Time not specified, defaulting to 5 minutes (300 seconds).",
                    ephemeral=True,
                )
            elif time > 21600:
                await interaction.response.send_message(
                    "Time cannot exceed 6 hours (21600 seconds).", ephemeral=True
                )
                return

            # Apply the mute (timeout) to the user
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
            # Inform the user if they lack permissions
            await interaction.response.send_message(
                f"{interaction.user.mention}, You do not have permission to use this command.",
                ephemeral=True,
            )

            print(
                f"Permission denied for mute command by {interaction.user.name} in guild {interaction.guild.name} ({interaction.guild.id})"
            )
