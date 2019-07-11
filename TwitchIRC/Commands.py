import _thread
import time

class BaseCommand():
    def __init__(self, *args, description="No description provided", usage="No usage provided", name="No name provided"):
        self.description = description
        self.usage = usage
        self.name = name

        self.setup(*args)
    
    def setup(self, *args):
        self.settings = args
    
    def __call__(self, message, bot):
        try:
            self.onexecute(bot, message)
        except Exception as e:
            print("Exception in Command")
            print(e)

    def onexecute(self, bot, message):
        print("Triggered default command handler for command '" + self.name + "'")


class Timer():
    def __init__(self, channels = "all", description="No description provided", name="No name provided"):
        self.channels = channels
        self.description = description
        self.name = name
    
    def __call__(self, interval, bot):
        self.bot = bot
        while True:
            try:
                self.onexecute()
            except Exception as e:
                Warning("[Timer] Failed! " + self.name + " see stacktrace below")
                print(e)
            
            time.sleep(interval * 60)
    
    def onexecute(self):
        print("Triggered default Timer '" + self.name + "'")