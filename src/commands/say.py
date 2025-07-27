from discord import app_commands, Interaction


def setup_say_command(bot, GUILD_ID):
    @bot.tree.command(
        name="say", description="Make the bot say something", guild=GUILD_ID
    )
    @app_commands.describe(message="The message for the bot to say")
    async def say_command(interaction: Interaction, message: str):
        if interaction.user.guild_permissions.manage_messages:
            await interaction.response.send_message("Message sent!", ephemeral=True)
            await interaction.channel.send(message)

            print(
                f"Say command used by {interaction.user.name} in guild {interaction.guild.name} ({interaction.guild.id})"
            )
            print(f"Message: {message}")
        else:
            await interaction.response.send_message(
                f"{interaction.user.mention}, You do not have permission to use this command.",
                ephemeral=True,
            )

            print(
                f"Prermission denied for say command by {interaction.user.name} in guild {interaction.guild.name} ({interaction.guild.id})"
            )
