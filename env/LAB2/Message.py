class Message(object):

    def __init__(self, fromId, toId, msg):
        self.fromId = fromId
        self.toId = toId
        self.msg = msg

    def Message(self):
        return self

    def __str__(self):
        return self.msg+" "+self.fromId
