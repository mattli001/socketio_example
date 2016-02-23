from socketIO_client import SocketIO, LoggingNamespace

import logging
logging.getLogger('requests').setLevel(logging.WARNING)
logging.basicConfig(level=logging.DEBUG)

def on_connect():
    print "on_connect()"

socketIO = SocketIO('localhost', 8001, LoggingNamespace)
print 'socketIO init done'
socketIO.on('connect', on_connect)

socketIO.wait(seconds=3)
print 'exit'
