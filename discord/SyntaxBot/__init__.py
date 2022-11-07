from nextcord.ext import commands
from nextcord import Interaction, Permissions
from .slash_commands import SlashCommands
from .event_listeners import Ready
from colors import cformat, CColors
import asyncio


guild_ids = [958457225096085534]

bot = commands.Bot()
slash = SlashCommands(bot)
bot.add_cog(slash)
bot.add_cog(Ready(bot))
bot.add_all_cog_commands()

@bot.slash_command(default_member_permissions=Permissions.moderate_members.flag,dm_permission=True)
async def toggle(interaction: Interaction):
    name = slash.qualified_name
    if bot.get_cog(name):
        on_off = False
        bot.remove_cog(name)
    else:
        on_off = True
        bot.add_cog(slash)
        
    await interaction.send(on_off and "on" or "off", ephemeral=True)
    
@bot.slash_command(default_member_permissions=Permissions.moderate_members.flag,dm_permission=True)
async def ephemeral(interaction: Interaction):
    await interaction.send(slash.ephemeral() and "on" or "off", ephemeral=True)
    


def init(token: str):
    print(f"\n\nStarting {cformat('SyntaxBot', CColors.MAGENTA)}®...")
    bot.run(token)
