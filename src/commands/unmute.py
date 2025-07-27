from discord import app_commands, Interaction, Member


def setup_unmute_command(bot, GUILD_ID):
    @bot.tree.command(
        name="unmute", description="Unmute a user in the server", guild=GUILD_ID
    )
    @app_commands.describe(user="The user to unmute")
    @app_commands.describe(reason="Reason for unmuting the user")
    async def unmute_command(
        interaction: Interaction, user: Member, reason: str = "No reason provided"
    ):
        # Check if the command user has permission to unmute members
        if interaction.user.guild_permissions.mute_members:

            # Check if the target user is currently muted
            if not user.is_timed_out():
                await interaction.response.send_message(
                    f"{user.mention} is not muted.", ephemeral=True
                )
                return

            # Remove the mute (timeout) from the user
            await user.timeout(
                None, reason=f"Unmuted by {interaction.user.name} for {reason}"
            )
            await interaction.response.send_message(
                f"{user.mention} has been unmuted.", ephemeral=True
            )

            print(
                f"Unmute command used by {interaction.user.name} in guild {interaction.guild.name} ({interaction.guild.id})"
            )
            print(f"Unmuted {user.name} with reason: {reason}")
        else:
            # Inform the user if they lack permissions
            await interaction.response.send_message(
                "You do not have permission to unmute members.", ephemeral=True
            )
