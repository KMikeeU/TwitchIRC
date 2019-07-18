from .Message import Message
from .User import User
import re

class UserMessage(Message):
    def parse(self):
        matches = re.match(r"^@badge-info=(.*?);badges=(.*?);color=(#[A-F0-9]+)?;display-name=(.*?);(?:emote-only=(\d);)?(?:emotes=([\d:\-,\/]*));flags=(.*?);id=([a-z0-9\-]+);mod=(\d);room-id=(\d+);subscriber=(\d+);tmi-sent-ts=(\d)+;turbo=(\d);user-id=(\d+);user-type=.*?\s:(\w+)!.*?@.*?\.tmi\.twitch\.tv\sPRIVMSG #(\w+)\s:(.*)$", self.raw)
        
        if matches == None:
            print("Error while parsing user message: " + self.raw)
            return

        self.type = "user"
        self.emote_only = matches.group(5)
        self.emotes = matches.group(6)
        self.flags = matches.group(7)
        self.message_id = matches.group(8)
        self.room_id = matches.group(10)
        self.timestamp = matches.group(12)
        self.channel = matches.group(16)
        self.content = matches.group(17)

        self.user = User(matches.group(15), matches.group(4), matches.group(14), matches.group(3), matches.group(9), matches.group(11), matches.group(2), matches.group(1), matches.group(13))
    
    def __str__(self):
        return self.user.username + "#" + self.channel + ": " + self.content