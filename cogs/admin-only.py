import discord
from discord.ext import commands

# https://gist.github.com/Painezor/eb2519022cd2c907b56624105f94b190


class AdminOnly(commands.Cog):
    """Ubbe only cog (for reloading bot)"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(hidden=True)
    async def load(self, ctx, *, message):
        """Loads a module."""
        try:
            self.bot.load_extension("cogs.{}".format(message))
        except Exception as e:
            embed = discord.Embed(
                color=0xE74C3C,
                description="\N{PISTOL}\n{}: {}".format(type(e).__name__, e),
            )
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(color=0xE74C3C, description="\N{OK HAND SIGN}")
            await ctx.send(embed=embed)

    @commands.command(hidden=True)
    async def unload(self, ctx, *, message):
        """Unloads a module."""
        if message == "admin-only":
            embed = discord.Embed(
                color=0xE74C3C, description="you cant unload the cog manager"
            )
            await ctx.send(embed=embed)
        else:
            try:
                self.bot.unload_extension("cogs.{}".format(message))
            except Exception as e:
                embed = discord.Embed(
                    color=0xE74C3C,
                    description="\N{PISTOL}\n{}: {}".format(type(e).__name__, e),
                )
                await ctx.send(embed=embed)
            else:
                embed = discord.Embed(color=0xE74C3C, description="\N{OK HAND SIGN}")
                await ctx.send(embed=embed)

    @commands.command(name="reload", hidden=True)
    async def _reload(self, ctx, *, message):
        """Reloads a module."""
        try:
            self.bot.reload_extension("cogs.{}".format(message))
        except Exception as e:
            embed = discord.Embed(
                color=0xE74C3C,
                description="\N{PISTOL}\n{}: {}".format(type(e).__name__, e),
            )
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(color=0xE74C3C, description="\N{OK HAND SIGN}")
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(AdminOnly(bot))
