__author__ = 'brennancrispin'

from autobahn.twisted.websocket import WebSocketServerProtocol

class EchohandlerProtocol(WebSocketServerProtocol):

    def __init__(self, factory):
        super(EchohandlerProtocol, self).__init__()
        self.factory = factory

    def onConnect(self, request):
        print "Client connecting: %s" % request.peer
        self.factory.connectionHandler.addConnection(request.peer, self)

    def onOpen(self):
        print "Websocket Connection Open"

    def onMessage(self, payload, isBinary):
        if isBinary:
            print("Binary message received: {} bytes").format(len(payload))
        else:
            print payload
            self.sendMessage(payload, isBinary)

    def onClose(self, wasClean, code, reason):
        print "Connection Closed: %s" % reason
