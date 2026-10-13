
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
        category = ctx.guild.get_channel(CATEGORY_ID)
        role = ctx.guild.get_role(ROLE_ID)

        if category is None:
            await ctx.send("❌ Safeguarding category not found.")
            return

        if role is None:
            await ctx.send("❌ Safeguarding role not found.")
            return

        if not isinstance(ctx.channel, discord.TextChannel):
            await ctx.send("❌ Use this command inside a ticket channel.")
            return

        await ctx.channel.edit(
            category=category,
            reason=f"Safeguarding escalation requested by {ctx.author}"
        )

        await ctx.send(
            f"🚨 **Ticket Escalated**\n"
            f"{role.mention} — please review this ticket.",
            allowed_mentions=discord.AllowedMentions(roles=True)
        )


async def setup(bot):
    await bot.add_cog(Safeguard(bot))
