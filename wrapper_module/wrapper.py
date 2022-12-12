# Created by Manuel Staufer [2022] Rights Reserved


from enum import Enum
import socket, time, asyncio, uuid


class WrapperType(Enum):
    GAME = 'game'
    DATABASE = 'database'


class Wrapper:
    def __init__(self, wrapper_type: WrapperType, maxUsers):
        self.json = {
            "uuid": uuid.uuid4(),
            "wrapper_type": wrapper_type,
            "maxUsers": maxUsers
        }


    def setType(self, wrapper_type: WrapperType):
        self.json['wrapper_type'] = wrapper_type


    def setMaxUsers(self, maxUsers):
        self.json['maxUsers'] = maxUsers


    def getType(self):
        return str(self.json['wrapper_type'].value)


    def getUUID(self):
        return str(self.json['uuid'])


    def getMaxUsers(self):
        return int(self.json['maxUsers'])


if __name__ == '__main__':
    pass