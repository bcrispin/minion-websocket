__author__ = 'brennancrispin'

from autobahn.twisted.websocket import WebSocketServerFactory
from EchoHandlerProtocol import EchohandlerProtocol
from ConnectionHandler import ConnectionHandler

class EchoHandlerFactory(WebSocketServerFactory):

    def __init__(self, url, debug=False):
        super(EchoHandlerFactory, self).__init__(url, debug)
        self.connectionHandler = ConnectionHandler()

    def buildProtocol(self, addr):
        protocol = EchohandlerProtocol(self)
        return protocol