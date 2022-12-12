# Created by Manuel Staufer [2022] Rights Reserved


class Permission:
    def __init__(self, perm_name: str, perm_status: bool):
        self.perm_name = perm_name
        self.perm_status = perm_status


    def setPermissionName(self, perm_name: str):
        self.perm_name = perm_name


    def setPermissionStatus(self, perm_status: bool):
        self.perm_status = perm_status


    def getPermission(self):
        return self.perm_name, self.perm_status


    def getPermissionName(self):
        return self.perm_name


    def getPermissionStatus(self):
        return self.perm_status