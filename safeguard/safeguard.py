
from discord.ext import commands
import discord

CATEGORY_ID = 1559625808140828742
ROLE_ID = 1559625565168730152


class Safeguard(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def safeguard(self, ctx):
        if ctx.guild is None:
            return

        category = ctx.guild.get_channel(CATEGORY_ID)
        role = ctx.guild.get_role(ROLE_ID)

        if category is None or role is None:
            await ctx.send("❌ Safeguarding category or role not found.")
            return

        if not isinstance(ctx.channel, discord.TextChannel):
            await ctx.send("❌ Use this command inside a ticket channel.")
            return

        from core.thread import Thread
        thread = await Thread.from_channel(ctx.channel)
        recipient = thread.recipient

        await ctx.channel.edit(
            category=category,
            reason=f"Safeguarded by {ctx.author}"
        )

        embed = discord.Embed(
            title="🚨 Ticket Escalated",
            description=(
                f"**Safeguarded by:** {ctx.author.mention}\n\n"
                f"{role.mention} — please review this ticket."
            ),
            color=discord.Color.red()
        )

        await ctx.send(
            embed=embed,
            allowed_mentions=discord.AllowedMentions(roles=True)
        )

        await recipient.send(
            embed=discord.Embed(
                title="Your ticket has been escalated",
                description=(
                    "Your ticket has been escalated to senior staff "
                    "for further review. The team will respond when "
                    "they are able to."
                ),
                color=discord.Color.red()
            )
        )


async def setup(bot):
    await bot.add_cog(Safeguard(bot))

