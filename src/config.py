from dotenv import dotenv_values
from os import path
import sys

__defaults = {
    "env": ".env.secret",
    "token": "TOKEN"
}


def is_venv():
    return (hasattr(sys, 'real_prefix') or
            (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix))


def get_token(dotenv_filename=__defaults["env"], token_name=__defaults["token"]):
    if not path.exists(dotenv_filename):
        return None

    if token_name not in dotenv_values(dotenv_filename):
        return None

    return dotenv_values(dotenv_filename)[token_name]
