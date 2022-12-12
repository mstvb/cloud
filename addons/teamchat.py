# Created by Manuel Staufer [2022] Rights Reserved


from addons.user import User


class TeamChat:
    def __init__(self):
        self.online = list()


class TeamChatUser(User):
    def __init__(self, username: str, password: str):
        super().__init__(username, password)
        self.loggedIn = False


    def setLoggedIn(self, loggedIn: bool):
        self.loggedIn = loggedIn


    def isLoggedIn(self):
        return self.loggedIn