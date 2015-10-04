__author__ = 'brennancrispin'

from Client import Client

class ConnectionHandler(object):
    def __init__(self):
        self.connections = {}

    def addConnection(self, connectionID, websocket):
        client = Client(connectionID, websocket)
        self.connections[connectionID] = client
        print self.connections

    def removeConnection(self, connectionID):
        if self.connectionInConnections(connectionID):
            del self.connctions[connectionID]

    def getConnection(self, connectionID):
        return self.connections.get(connectionID, False)

    def getAllConnections(self):
        return self.connections

    def connectionInConnections(self, connectionID):
        return connectionID in self.connections