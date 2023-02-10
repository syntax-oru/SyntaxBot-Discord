from nextcord import Interaction, SlashOption, slash_command
from nextcord.ext import commands

_first_name = SlashOption(
    name='förnamn',
    description='Det namnet du angav som förnamn på medlemsansökan',
    min_length=1,
    required=True,
    verify=True,
)

_last_name = SlashOption(
    name='efternamn',
    description='Det namnet du angav som efternamn på medlemsansökan',
    min_length=1,
    required=True,
    verify=True,
)

_engineer_type = SlashOption(
    name='ingenjörstyp',
    description='Går du civilingenjör eller högskoleingenjör?',
    choices=['Civilingenjör', 'Högskoleingenjör'],
    required=True,
    verify=True,
)

_engineer_types = ['Civilingenjör', 'Högskoleingenjör',]

_civil_program_choices = [
    'Datateknik',
    'Industriell Ekonomi',
]

_hogskole_program_choices = _civil_program_choices + [
    'Industriell Design och Produktutveckling',
    'Maskinteknik',
    'Byggteknik',
]

_program_option = SlashOption(
    name='program',
    description='Vilket program går du?',
    choices=['Civilingenjör, ' + program for program in _civil_program_choices] + ['Högskoleingenjör, ' + program for program in _hogskole_program_choices],
    # autocomplete=True,
    required=True,
    verify=True,
)

class BliMedlem(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @slash_command(name='blimedlem')
    async def blimedlem(
        self,
        interaction: Interaction,
        name: str = _first_name,
        surname: str = _last_name,
        # engineer_type: str = _engineer_type,
        program: str = _program_option
    ):
        await interaction.response.send_message(
# engineer type: {engineer_type}
f"""```
name:          {name}
surname:       {surname}
program:       {program}
```"""
        )

    # @blimedlem.on_autocomplete("program")
    # async def program_autocomplete(self, interaction: Interaction, program: str, engineer_type: str):
    #     print(engineer_type)
    #     if engineer_type== 'Civilingenjör':
    #         await interaction.response.send_autocomplete(_civil_program_choices)
    #     else:
    #         await interaction.response.send_autocomplete(_hogskole_program_choices)