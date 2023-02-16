# Created by Manuel Staufer [2022] Rights Reserved
import types
from enum import Enum
from addons.console import ConsoleStyle, getStyle
import socket, time, asyncio, uuid


""" 
    TODO:
    - REGISTER USERS
    - COMMUNICATION WITH WRAPPERS
    - COMMANDS FOR CLOUD
    - DYNAMIC SYSTEM
"""


class Master:
    def __init__(self):
        self.json = {'uuid': uuid.uuid4(), 'wrappers': list()}


    def getUUID(self):
        return self.json['uuid']


    def getWrappers(self):
        return self.json['wrappers']


if __name__ == '__main__':
    m = Master()
    print(f'{getStyle(ConsoleStyle.GRAY)}UUID: {getStyle(ConsoleStyle.RED) + str(m.getUUID())}')