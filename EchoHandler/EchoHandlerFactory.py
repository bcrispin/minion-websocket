__author__ = 'brennancrispin'

from autobahn.twisted.websocket import WebSocketServerFactory
from EchoHandlerProtocol import EchohandlerProtocol
from Client import Client

class EchoHandlerFactory(WebSocketServerFactory):

    connections = {}

    def buildProtocol(self, addr):
        protocol = EchohandlerProtocol(self)
        return protocol

    def addConnection(self, connectionID, websocket):
        client = Client(connectionID, websocket)
        self.connections[connectionID] = client
        print self.connections

    def removeConnection(self, connectionID):
        del self.connctions[connectionID]

    def getConnection(self, connectionID):
        return self.connections.get(connectionID, False)

    def getAllConnections(self):
        return self.connections