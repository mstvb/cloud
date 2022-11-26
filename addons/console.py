# Created by Manuel Staufer [2022] Rights Reserved


from enum import Enum


class ConsoleColor(Enum):

    BOLD = '\33[1m'
    ITALIC = '\33[3m'
    BLINK = '\33[5m'

    GREEN = '\33[32m'
    BLUE = '\33[34m'
    RED = '\33[31m'


def getStyle(style: ConsoleColor):
    return style.value