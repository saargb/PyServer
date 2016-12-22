from socket import *
from thread import *

size = 2048

def send(msg):
    print name + '::' + msg + '::' + '0'
    socket.send(name + '::' + msg + '::' + recipient + '\n')

def send_raw(msg):
    socket.send(msg + '\n')

def update_recipient(recipient_name):
    recipient = recipient_name

socket = socket(AF_INET, SOCK_STREAM)
socket.connect(('', 4444))
name = socket.recv(size)
recipient = name

def isRequestingNameChange()

while True:
    str = raw_input('>> ')
    send(str)
    print socket.recv(size)
socket.close()
