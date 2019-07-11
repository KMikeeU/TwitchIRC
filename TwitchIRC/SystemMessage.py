from .Message import Message

class SystemMessage(Message):
    def parse(self):
        self.type = "system"
        if self.raw == ":tmi.twitch.tv NOTICE * :Login authentication failed":
            print("Login failed!")