import _thread

class CommandHandler():
    def __init__(self, bot):
        self.commands = {}
        self.timers = []
        self.bot = bot
    
    def registerCommand(self, trigger, _callable):
        self.commands[trigger] = _callable
        _callable.bot = self.bot

    def registerTimer(self, interval, timer):
        self.timers.append(timer)
        _thread.start_new_thread(timer, (interval, self.bot))

    def __call__(self, message):
        args = message.content.split(" ")
        trigger = args[0][len(self.bot.prefix):]


        if trigger in self.commands:
            _thread.start_new_thread(self.commands[trigger], (message, self.bot))
        else:
            print("User '" + message.user.username + "' executed unknown command '" + trigger + "' in channel '" + message.channel + "'")