import TwitchIRC

bot = TwitchIRC.Bot()                                   # Creates new bot instance
bot.connect()                                           # Connects to Twitch
bot.login("Bot_Username", "oauth:Twitch_OAuth_Key")     # Logs in with user credentials
bot.join("clintstevens")

def onMessage(bot, message):                            # Defining what should happen when a message is received
    print(message)

bot.messageHandler.register(onMessage)                  # Adding custom function to the bot

bot.listen()                                            # Listening for new messages in the background

while True:                                             # ... do something else
    input("")