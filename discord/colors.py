# Credit: J.Hadida (jhadida87 at ggooglemail) https://gist.github.com/Sheljohn/68ca3be74139f66dbc6127784f638920
import random
from typing import Tuple, Any

ccolors = ["k", "r", "g", "y", "b", "m", "c", "w"]
cstyles = ["b", "i", "u", "s", "x", "r", "y", "f", "h"]


class CColors:
    BLACK = "k"
    RED = "r"
    GREEN = "g"
    YELLOW = "y"
    BLUE = "b"
    MAGENTA = "m"
    CYAN = "c"
    WHITE = "w"


class CStyles:
    BOLD = "b"
    ITALIC = "i"
    UNDERLINE = "u"
    STRIKETHROUGH = "s"
    BLINKING = "x"
    REVERSE = "r"
    FAST_BLINKING = "y"
    FAINT = "f"
    HIDE = "h"


def __randfmt(fmt: list[str], exclude: list[str] = None) -> str:
    if exclude is None:
        exclude = []
    _include = [_fmt for _fmt in fmt if _fmt not in exclude]
    return _include[random.randrange(0, len(_include))]


def randcolor(exclude: list[str] = None) -> str:
    return __randfmt(ccolors, exclude)


def randstyle(exclude: list[str] = None) -> str:
    return __randfmt(cstyles, exclude)


def __randfgbg() -> tuple[str, str]:
    return randcolor(), randcolor()


def randfgbg() -> tuple[str, str]:
    fg, bg = __randfgbg()
    while fg == bg:
        fg, bg = randfgbg()

    return fg, bg


def randfmt(fmt: str, fg=True, bg=True, styles=True) -> str:
    _fg, _bg, _styles = None, None, None
    if fg:
        _fg = randcolor()
    if bg:
        _bg = randcolor()
    if styles:
        _styles = randstyle()
    return cformat(fmt, _fg, _bg, _styles)


def cformat(fmt: str, fg=None, bg=None, style=None) -> str:
    """
    Colour-printer.

        cprint( 'Hello!' )                                  # normal
        cprint( 'Hello!', fg='g' )                          # green
        cprint( 'Hello!', fg='r', bg='w', style='bx' )      # bold red blinking on white

    List of colours (for fg and bg):
        k   black
        r   red
        g   green
        y   yellow
        b   blue
        m   magenta
        c   cyan
        w   white

    List of styles:
        b   bold
        i   italic
        u   underline
        s   strikethrough
        x   blinking
        r   reverse
        y   fast blinking
        f   faint
        h   hide
    """

    COLCODE = {
        'k': 0,  # black
        'r': 1,  # red
        'g': 2,  # green
        'y': 3,  # yellow
        'b': 4,  # blue
        'm': 5,  # magenta
        'c': 6,  # cyan
        'w': 7  # white
    }

    FMTCODE = {
        'b': 1,  # bold
        'f': 2,  # faint
        'i': 3,  # italic
        'u': 4,  # underline
        'x': 5,  # blinking
        'y': 6,  # fast blinking
        'r': 7,  # reverse
        'h': 8,  # hide
        's': 9,  # strikethrough
    }

    # properties
    props = []
    if isinstance(style, str):
        props = [FMTCODE[s] for s in style]
    if isinstance(fg, str):
        props.append(30 + COLCODE[fg])
    if isinstance(bg, str):
        props.append(40 + COLCODE[bg])

    # display
    props = ';'.join([str(x) for x in props])
    if props:
        return str('\x1b[%sm%s\x1b[0m' % (props, fmt))
    else:
        return fmt


def cprint(fmt: str, fg=True, bg=True, styles=True):
    print(cformat(fmt, fg, bg, styles))
