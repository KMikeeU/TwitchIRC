

class Message():
    def __init__(self):
        self.type = "generic"
    
    def __call__(self, raw):
        self.raw = raw

        self.parse()
        
        return self

    def parse(self):
        pass