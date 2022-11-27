# Created by Manuel Staufer [2022] Rights Reserved


from enum import Enum


class ConsoleStyle(Enum):

    BOLD = '\33[1m'
    ITALIC = '\33[3m'

    GREEN = '\33[32m'
    BLUE = '\33[34m'
    RED = '\33[31m'


def getStyle(style: ConsoleStyle):
    return style.value