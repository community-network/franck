"""discord api connection"""

import discord
from discord.ext import commands
import discordhealthcheck

"""for --token args"""
import argparse

# make the arg --token available
parser = argparse.ArgumentParser()
parser.add_argument(
    "--token",
    help="Get your own token here - https://discordapp.com/developers/applications/",
)
args = parser.parse_args()

# replace args.token with "discord-token" if you dont want to run this in pterodactyl
TOKEN = args.token

bot = commands.Bot(command_prefix="")
bot.remove_command("help")
bot.load_extension("cogs.franck")
bot.load_extension("cogs.admin-only")
discordhealthcheck.start(bot)


@bot.event
async def on_ready():
    print("bot started \n")


# dont give a error if a command doesn't exist
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        return
    elif isinstance(error, commands.MissingRequiredArgument):
        return
    elif isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(
            color=0xE74C3C, description="Your not allowed to use this command"
        )
        await ctx.send(embed=embed)
    raise error


# run the bot
bot.run(TOKEN)
