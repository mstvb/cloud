# Created by Manuel Staufer [2022] Rights Reserved


""" IMPORT MODULES """
from enum import Enum
import socket, time, asyncio, uuid


class WrapperType(Enum):
    GAME = 'game'
    DATABASE = 'database'


class Wrapper:
    def __init__(self, wrapper_type: WrapperType, maxUsers):
        self.wrapper_uuid = uuid.uuid4()
        self.wrapper_type = wrapper_type
        self.maxUsers = maxUsers


    def getType(self):
        return self.wrapper_type.value


    def getUUID(self):
        return str(self.wrapper_uuid)


if __name__ == '__main__':
    pass