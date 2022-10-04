from nextcord.ext import commands
from .slash_commands import SlashCommands
from .event_listeners import Ready
from colors import cformat, CColors
import asyncio


guild_ids = [958457225096085534]

bot = commands.Bot()
bot.add_cog(SlashCommands(bot))
bot.add_cog(Ready(bot))
bot.add_all_cog_commands()


def init(token: str):
    print(f"\nStarting {cformat('SyntaxBot', CColors.MAGENTA)}®...")
    bot.run(token)
