from threading import Thread
from socket import socket

size = 2048

class ClientIO(Thread):
    def __init__(self, socket, request_queue):
        Thread.__init__(self)
        self.socket = socket
        self.request_queue = request_queue
    def run(self):
        while True:
            str = self.socket.recv(size)
            print 'Debug: the raw, recieved string: ', str
            self.request_queue.put(str)
    def send(self, msg):
        self.socket.send(msg)