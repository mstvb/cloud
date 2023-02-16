# Created by Manuel Staufer [2022] Rights Reserved


from enum import Enum
from addons.console import ConsoleStyle, getStyle
import socket, time, asyncio, uuid


""" 
    TODO:
    - REGISTER USERS
    - COMMUNICATION WITH WRAPPERS
    - COMMANDS FOR CLOUD
    - DYNAMIC
"""


class Master:
    def __init__(self):
        self.json = {'uuid': uuid.uuid4()}


    def getUUID(self):
        return str(self.json['uuid'])


if __name__ == '__main__':
    m = Master()
    print(f'{getStyle(ConsoleStyle.GRAY)}UUID: {getStyle(ConsoleStyle.RED) + m.getUUID()}')