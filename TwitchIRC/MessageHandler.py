

class MessageHandler():
    def __init__(self, bot):
        self.handlers = []
        self.bot = bot
    
    def register(self, handler):
        self.handlers.append(handler)
    
    def handle(self, UserMessage):
        for handler in self.handlers:
            handler(self.bot, UserMessage)