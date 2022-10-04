import nextcord
from nextcord.ext import commands
from colors import *


class Ready(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.syntax = cformat("SyntaxBot", fg=CColors.MAGENTA, style=CStyles.BOLD) + "®"

    @commands.Cog.listener()
    async def on_connect(self):
        print(f"{self.syntax} is {cformat('connected', fg=CColors.YELLOW, style=CStyles.BOLD)} to the Discord API "
              f"websocket, waiting for {cformat('ready', fg=CColors.GREEN, style=CStyles.ITALIC)}...")

    @commands.Cog.listener()
    async def on_ready(self):
        ready = cformat("ready!", fg=CColors.GREEN, style=CStyles.BOLD)
        print(f"{self.syntax} is {ready}")

    @commands.Cog.listener()
    async def on_disconnect(self):
        print(f"{self.syntax} was {cformat('disconnected', fg=CColors.RED, style=CStyles.BOLD)}!")

    @commands.Cog.listener()
    async def on_resume(self):
        print(f"{self.syntax} has {cformat('reconnected', fg=CColors.GREEN, style=CStyles.BOLD)}!")

    @commands.Cog.listener()
    async def on_close(self):
        print(f"{self.syntax} has been {cformat('shutdown', fg=CColors.RED, style=CStyles.BOLD)}! Goodbye!")

    @commands.Cog.listener()
    async def on_error(self):
        print(f"{self.syntax} has encountered an {cformat('error', fg=CColors.RED, style=CStyles.BOLD)}!")
        raise

    @commands.Cog.listener()
    async def on_member_join(self, member: nextcord.Member):
        localization = {
            "en-US": "Did you know I exist? It's true! If you want to help develop me, join the Marketing Committee!",
            "sv-SE": "Visste du jag existerar? De sant! Om du vill hjälpa till å utveckla mig, ansök till "
                     "Marknadsföringsutskottet!"
        }

        link = "https://syntax.teknat.se/?page_id=690"
        locale = "en-US"
        if member.guild.preferred_locale in localization.keys():
            locale = member.guild.preferred_locale

        dm = await member.create_dm()
        await dm.send(localization[locale] + link)
