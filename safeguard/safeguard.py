
from discord.ext import commands


class Safeguard(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def safeguard(self, ctx):
        await ctx.send(
            "🚨 **Ticket Escalated**\n"
            "Please configure the safeguarding category "
            "and role before using this command."
        )


async def setup(bot):
    await bot.add_cog(Safeguard(bot))
