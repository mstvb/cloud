# Created by Manuel Staufer [2022] Rights Reserved


""" IMPORT MODULES """
from enum import Enum
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
    print(m.getUUID())