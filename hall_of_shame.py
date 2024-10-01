import discord
from discord import app_commands
from discord.ext import commands

class HallOfShame(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="add_shame", description="Add a user to the Hall of Shame with an optional photo")
    @app_commands.checks.has_permissions(administrator=True)
    async def add_shame(
        self, 
        interaction: discord.Interaction, 
        member: discord.Member, 
        reason: str = "No reason provided", 
        image: discord.Attachment = None
    ):
        """Add a user to the Hall of Shame with an optional photo."""
        # Create an embed to display the shame entry
        embed = discord.Embed(
            title=f"{member.display_name} has been added to the Hall of Shame!",
            description=f"**Reason:** {reason}",
            color=discord.Color.dark_red()
        )
        embed.set_author(name=interaction.user.display_name, icon_url=interaction.user.avatar.url)
        embed.set_thumbnail(url=member.avatar.url)

        # Attach the image if one was uploaded
        if image:
            embed.set_image(url=image.url)

        # Send the embed to the channel where the command was used
        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(HallOfShame(bot))
