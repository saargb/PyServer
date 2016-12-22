from socket import *
from thread import *

def is_requesting_name_change(st):
    '''
    st:str
    :param str:
    :return:the name to be updated, if and only if st starts with 'update name to ' and ends with a name.
    '''
    if st.startswith('update name to ') and st[15 : ].isalpha():
        return st[15 : ]
    return None

def is_requesting_recipient_update(st):
    if st.startswith('connect me to ') and st[14 : ].isalpha():
        return st[14]
    return None

def send_to_user(msg):
    print name + '::' + msg + '::' + recipient
    socket.send(name + '::' + msg + '::' + recipient + '\n')

def send_raw(msg):
    socket.send(msg + '\n')

size = 2048
socket = socket(AF_INET, SOCK_STREAM)
socket.connect(('', 4444))
name = socket.recv(size)
recipient = name

while True:
    st = raw_input('>> ')
    name_request = is_requesting_name_change(st)
    recipient_request = is_requesting_recipient_update(st)
    if name_request:
        name = name_request
        send_raw(name + '::' + name + '::00000001')
    elif recipient_request:
        recipient = recipient_request
        #no need to update the server, it doesn't know who the client is talking to.
    else:
        send_to_user(st)
    print socket.recv(size)
socket.close()
