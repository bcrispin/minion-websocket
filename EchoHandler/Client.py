__author__ = 'brennancrispin'



class Client(object):
    def __init__(self, clientAddress, websocket):
        self.websocket = websocket
        self.clientAddress = clientAddress
        self.clientID = ""
        self.targetIDs = []

    def getSocket(self):
        return self.websocket

    def getClientAddress(self):
        return self.clientAddress

    def getClientID(self):
        return self.clientID

    def getTargetIDs(self):
        return self.targetIDs

    def setClientID(self, clientID):
        self.clientID = clientID

    def addTargetID(self, targetID):
        if targetID not in self.targetIDs:
            self.targetIDs.append(targetID)

    def removeTargetID(self, targetID):
        if targetID in self.targetIDs:
            self.targetIDs.remove(targetID)

    def sendMessage(self, message, isBinary=False):
        self.websocket.sendMessage(message, isBinary)