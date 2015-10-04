__author__ = 'brennancrispin'

from EchoHandler.EchoHandlerProtocol import EchohandlerProtocol
from EchoHandler.EchoHandlerFactory import EchoHandlerFactory

from twisted.internet import reactor

if __name__ == "__main__":

    factory = EchoHandlerFactory("ws://127.0.0.1:9000", debug=False)

    reactor.listenTCP(9000, factory)
    reactor.run()

