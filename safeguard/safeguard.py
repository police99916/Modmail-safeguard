import discord
from discord.ext import commands

CATEGORY_ID = 1559625808140828742
ROLE_ID = 1559625565168730152


class Safeguard(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="safeguard")
    async def safeguard(self, ctx):
        if ctx.guild is None or not isinstance(ctx.channel, discord.TextChannel):
            return

        category = ctx.guild.get_channel(CATEGORY_ID)
        role = ctx.guild.get_role(ROLE_ID)

        if not isinstance(category, discord.CategoryChannel) or role is None:
            return

        thread = self.bot.threads.get(ctx.channel.id)

        if thread is None:
            return

        recipient = thread.recipient

        await ctx.channel.edit(
            category=category,
            reason=f"Safeguarded by {ctx.author}"
        )

        embed = discord.Embed(
            title="🚨 Ticket Escalated",
            description=(
                f"**Safeguarded by:** {ctx.author.mention}\n"
                f"**Senior Staff:** {role.mention}\n\n"
                "Safeguarding, please review this ticket."
            ),
            color=discord.Color.red()
        )

        await ctx.send(
            content=role.mention,
            embed=embed,
            allowed_mentions=discord.AllowedMentions(
                roles=True,
                users=True
            )
        )

        try:
            await recipient.send(
                embed=discord.Embed(
                    title="Your ticket has been escalated",
                    description=(
                        "Your ticket has been escalated to our Safeguarding Team "
                        "for further review. The team will respond when "
                        "they are able to."
                    ),
                    color=discord.Color.red()
                )
            )
        except (discord.Forbidden, discord.HTTPException):
            pass


async def setup(bot):
    await bot.add_cog(Safeguard(bot))
