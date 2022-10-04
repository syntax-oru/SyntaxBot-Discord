import asyncio

import SyntaxBot
from config import *
from os import path
from colors import *


class __Defaults:
    env_file: str
    is_venv: bool
    req_installed: bool
    first_time: bool
    authors = "../AUTHORS"


def welcome():
    authors = __Defaults.authors
    msg = f"Welcome to {cformat('SyntaxBot', fg=CColors.MAGENTA, style=CStyles.BOLD)}®"

    if path.exists(authors):
        with open(authors, "r") as file:
            msg += ", made by:\n"
            for line in file:
                msg += "    " + \
                    cformat(line, fg=randcolor([CColors.BLACK, CColors.MAGENTA]), style=randstyle(CStyles.STRIKETHROUGH)) \
                    + "    "
    else:
        msg += "!"

    print(msg)


if __name__ == "__main__":
    welcome()
    SyntaxBot.init(get_token("../.env.secret"))
