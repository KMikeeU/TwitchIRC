import socket
import _thread
import ssl
from .SystemMessage import SystemMessage
from .UserMessage import UserMessage
from . import CommandHandler
from . import MessageHandler

class Bot():
    def __init__(self, prefix="!"):
        self.prefix = prefix
        self.commandHandler = CommandHandler.CommandHandler(self)
        self.messageHandler = MessageHandler.MessageHandler(self)
        self.channels = []

    def connect(self):
        # Connecting to Twitch IRC socket
        context = ssl.create_default_context()

        try:
            sock = socket.create_connection(("irc.chat.twitch.tv", 6697))
        except:
            Exception("Could not connect to Twitch IRC")

        self.socket = context.wrap_socket(sock, server_hostname="irc.chat.twitch.tv")

    def login(self, username, oauth):
        # logging in
        self.sendraw("PASS " + oauth)
        self.sendraw("NICK " + username)

        # Sending capabilitiy request
        self.send_cap()

    
    # Twitch specific capabilities, chat interactions
    def join(self, channel):
        self.sendraw("JOIN #"+channel)
        self.channels.append(channel)
    
    def part(self, channel):
        self.sendraw("PART #"+channel)
        self.channels.remove(channel)

    def send(self, channels, message):
        if channels == "all":
            channels = self.channels

        if type(channels) == str:
            self.sendraw("PRIVMSG #"+channels+" :"+message)

        if type(channels) == list:
            for channel in channels:
                self.send(channel, message)
        
        
    
    def whisper(self, channel, user, message):
        self.sendraw("PRIVMSG #"+channel+" :"+"/w " + user + " " + message)

    def pong(self):
        self.sendraw("PONG :tmi.twitch.tv")

    def send_cap(self):
        self.sendraw("CAP REQ :twitch.tv/tags")

    # Socket level interactions
    def sendraw(self, message):
        self.socket.send(message.encode("UTF-8") + b"\r\n")

    def receive_loop(self):
        d = b""
        while True:
            try:
                d += self.socket.recv(16)
            except KeyboardInterrupt:
                return
            
            if b"\r\n" in d:
                d = d.split(b"\r\n")
                message = d[0]
                message = message.decode("UTF-8")

                self.onMessage(message)

                d = d[1]

    def listen(self):
        _thread.start_new_thread(self.receive_loop, ())

    # Messages
    def onMessage(self, rawmessage):
        if rawmessage == "PING :tmi.twitch.tv":
            self.pong()
            return
        
        if rawmessage.startswith(":"):
            message = SystemMessage()
        
        elif rawmessage.startswith("@"):
            message = UserMessage()

        try:
            message(rawmessage)
        except Exception as e:
            print(e)
            return
        
        if type(message) == UserMessage:
            self.messageHandler.handle(message)
            if message.content.startswith(self.prefix):
                try:
                    self.commandHandler(message)
                except Exception as e:
                    print("Exception while starting commandHandler on message: \n" + str(message))
                    print(e)

            # print(str(message))