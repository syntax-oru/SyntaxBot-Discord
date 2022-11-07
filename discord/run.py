import SyntaxBot
from os import getenv
from colors import *

def get_token() -> str:
    token = getenv("TOKEN")
    if not token:
        cprint("No TOKEN found in environment variables, exiting...", CColors.RED)
        while True:
            pass
    return token

def welcome():
    msg = f"Welcome to {cformat('SyntaxBot', fg=CColors.MAGENTA, style=CStyles.BOLD)}®"

    with open("AUTHORS") as authors:
        msg += ", made by:\n"
        for author in authors.readlines():
            msg += "    " + \
                cformat(author, fg=randcolor([CColors.BLACK, CColors.MAGENTA]), style=randstyle(CStyles.STRIKETHROUGH)) \
                + "    "
                
        print(msg)


if __name__ == "__main__":
    welcome()
    SyntaxBot.init(get_token())
