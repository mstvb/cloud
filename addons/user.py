# Created by Manuel Staufer [2022] Rights Reserved


from addons.permission import Permission
import uuid


class User:
    def __init__(self, username: str, password: str):
        self.json = {"username": username,
                     "pass": password,
                     "uuid": uuid.uuid4()
                    }
        self.permissions = []


    def setUsername(self, username: str):
        self.json['username'] = username


    def setPassword(self, password: str):
        self.json['password'] = password


    def addPermission(self, perm: Permission):
        self.permissions.append(perm)


    def deletePermission(self, perm_name: str):
        for perm in self.permissions:
            if perm.getPermissionName is perm_name:
                del perm


    def getUsername(self):
        return self.json['username']


    def getPassword(self):
        return self.json['pass']


    def getUUID(self):
        return self.json['uuid']


    def hasPermission(self, perm_name: str):
        for perm in self.permissions:
            if perm.getPermissionName is perm_name:
                return perm