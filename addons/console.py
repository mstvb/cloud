# Created by Manuel Staufer [2022] Rights Reserved


from enum import Enum


class ConsoleStyle(Enum):

    BOLD = '\33[1m'
    ITALIC = '\33[3m'

    RED = '\33[31m'
    GREEN = '\33[32m'
    YELLOW = '\33[33m'
    BLUE = '\33[34m'
    PURPLE = '\33[35m'
    LIGHT_GRAY = '\33[36m'
    GRAY = '\33[37m'
    WHITE = '\33[38m'



def getStyle(style: ConsoleStyle):
    return style.value