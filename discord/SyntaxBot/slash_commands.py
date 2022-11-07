import nextcord
from nextcord.ext import commands
from colors import *


class Localization:
    # Languages
    DANISH = "da"
    GERMAN = "de"
    ENGLISH_TRADITIONAL = "en-GB"
    ENGLISH_SIMPLIFIED = "en-US"
    SPANISH = "es-ES"
    FRENCH = "fr"
    CROATIAN = "hr"
    ITALIAN = "it"
    LITHUANIAN = "lt"
    HUNGARIAN = "hu"
    DUTCH = "nl"
    NORWEGIAN = "no"
    POLISH = "pl"
    PORTUGUESE = "pt-BR"
    ROMANIAN = "ro"
    FINNISH = "fi"
    SWEDISH = "sv-SE"
    VIETNAMESE = "vi"
    TURKISH = "tr"
    CZECH = "cs"
    GREEK = "el"
    BULGARIAN = "bg"
    RUSSIAN = "ru"
    UKRAINIAN = "uk"
    HINDI = "hi"
    THAI = "th"
    CHINESE = "zh-CN"
    JAPANESE = "ja"
    TAIWANESE = "zh-TW"
    KOREAN = "ko"

    __locales = {
        "da": "Dansk",
        "de": "Deutsch",
        "en-GB": "English, UK",
        "en-US": "English, US",
        "es-ES": "Español",
        "fr": "Français",
        "hr": "Hrvatski",
        "it": "Italiano",
        "lt": "Lietuviškai",
        "hu": "Magyar",
        "nl": "Nederlands",
        "no": "Norsk",
        "pl": "Polski",
        "pt-BR": "Português do Brasil",
        "ro": "Română",
        "fi": "Suomi",
        "sv-SE": "Svenska",
        "vi": "Tiếng Việt",
        "tr": "Türkçe",
        "cs": "Čeština",
        "el": "Ελληνικά",
        "bg": "български",
        "ru": "Pусский",
        "uk": "Українська",
        "hi": "हिन्दी",
        "th": "ไทย",
        "zh-CN": "中文",
        "ja": "日本語",
        "zh - TW": "繁體中文",
        "ko": "한국어",
    }

    def __init__(self, default, name: str|dict[str: str], description: str|dict[str: str] = None):
        self.__default = default
        self.__names = {}
        self.__descriptions = {}

        Localization.is_valid_locale(default)
        if isinstance(name, dict):
            self.add_names(name)
        else:
            self.add_name(default, name)

        if description:
            if isinstance(description, dict):
                self.add_descriptions(description)
            else:
                self.add_description(default, description)

    @staticmethod
    def is_valid_locale(locale: str, raise_error: bool = False) -> bool:
        if locale in Localization.__locales:
            return True
        elif raise_error:
            raise ValueError(f"Unsupported locale: {cformat(locale, fg=CColors.RED, style=CStyles.UNDERLINE)}"
                             f"See https://discord.com/developers/docs/reference#locales for supported locales")
        return False

    def __add_localizations(self, localizations: dict[str: str], name: bool):
        unsupported_locales = []
        for locale in localizations.keys():
            if not Localization.is_valid_locale(locale):
                unsupported_locales.append(cformat(locale, CColors.RED))
        if unsupported_locales:
            raise ValueError(f"Unsupported locales: {str.join(', ', unsupported_locales)}")

        if name:
            self.__names.update(localizations)
        else:
            self.__descriptions.update(localizations)

    def __add_localization(self, locale: str, localization: str, name: bool):
        Localization.is_valid_locale(locale, True)
        if name:
            self.__names[locale] = localization
        else:
            self.__descriptions[locale] = localization

    def __get_localization(self, locale: str, name: bool) -> str:
        Localization.is_valid_locale(locale, True)
        localizations = name and self.__names or self.__descriptions
        if locale not in localizations.keys():
            return localizations[self.__default]
        else:
            return localizations[locale]

    def add_name(self, locale: str, localization: str):
        self.__add_localization(locale, localization, True)

    def add_names(self, localizations: dict[str: str]):
        self.__add_localizations(localizations, True)

    def add_description(self, locale: str, localization: str):
        self.__add_localization(locale, localization, False)

    def add_descriptions(self, localizations: dict[str: str]):
        self.__add_localizations(localizations, False)

    def name(self, locale) -> str:
        return self.__get_localization(locale, True)

    def description(self, locale) -> str:
        return self.__get_localization(locale, False)

    def names(self) -> dict[str: str]:
        return self.__names

    def descriptions(self) -> dict[str: str]:
        return self.__descriptions


_whoami_localization = {
    "name": {
        "en-US": "whoami",
        "sv-SE": "vemädet",
    }, "description": {
        "en-US": "Wait... Syntax has a Discord bot?",
        "sv-SE": "Vänta... sen när har Syntax en Discord bot?",
    }, "answer": {
        "en-US": "It's true! If you want to help develop me, join the Marketing Committee!",
        "sv-SE": "De sant! Om du vill hjälpa till å utveckla mig, ansök till Marknadsföringsutskottet!",
    },
}


class SlashCommands(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.__ephemeral = True
        
    def ephemeral(self) -> bool:
        self.__ephemeral = not self.__ephemeral
        return self.__ephemeral

    @nextcord.slash_command(name_localizations=_whoami_localization["name"],
                            description_localizations=_whoami_localization["description"])
    async def whoami(self, interaction: nextcord.Interaction):
        link = "https://syntax.teknat.se/?page_id=690"
        key = interaction.locale in _whoami_localization['answer'].keys() and interaction.locale or "en-US"
        await interaction.send(f"{_whoami_localization['answer'][key]} {link}", ephemeral=self.__ephemeral) 