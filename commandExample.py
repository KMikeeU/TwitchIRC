import TwitchIRC

bot = TwitchIRC.Bot()                                                   # Creates new bot instance with custom command prefix (default: !)
bot.connect()                                                           # Connects to Twitch
bot.login("Bot_Username", "oauth:Twitch_OAuth_Key")                     # Logs in with user credentials
bot.join("clintstevens")

class myCommand(TwitchIRC.Commands.BaseCommand):                        # Creating a custom command
    def onexecute(self, bot, message):
        bot.send(message.channel, "Hello " + message.user.username)     # Responds "Hello" followed by the username of the user who triggered the command


bot.commandHandler.registerCommand("hello", myCommand())                # Adding custom functionality to the bot

bot.listen()                                                            # Listening for new messages in the background


while True:                                                             # ... do something else
    input("")