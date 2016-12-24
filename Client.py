from socket import *
from thread import *

def is_requesting_name_change(st):
    '''
    st:str
    :param str:
    :return:the name to be updated, if and only if st starts with 'update name to ' and ends with a name.
    '''
    if st.startswith('update name to ') and st[15 : ].isalnum():
        return st[15 : ]
    return None

def is_requesting_recipient_update(st):
    if st.startswith('connect me to ') and st[14 : ].isalnum():
        return st[14]
    return None

def send_to_user(msg):
#    print name + '::' + msg + '::' + recipient
    socket.send(name + '::' + msg + '::' + recipient + '\n')

def send_raw(msg):
    socket.send(msg + '\n')

size = 2048
socket = socket(AF_INET, SOCK_STREAM)
socket.connect(('', 4000))
name = socket.recv(size)
recipient = name

while True:
#    print 'Debug: raw input!'
    st = raw_input('>> ')
    name_request = is_requesting_name_change(st)
#    print 'Debug: cheking for name request'
    recipient_request = is_requesting_recipient_update(st)
#    print 'Debug: cheking for recipient request'
    if name_request:
        print 'Debug: Changing name!'
        send_raw(name + '::' + name_request + '::00000001')
        name = name_request
        print socket.recv(size)
    elif recipient_request:
#        print 'Debug: Changing recipient!'
        recipient = recipient_request
        print 'Your recipient has been updated!'
        #no need to update the server, it doesn't know who the client is talking to.
    else:
#        print 'Debug: sending message!'
        send_to_user(st)
#        print 'Debug: message sent!'
        print socket.recv(size)
#        print 'Debug: Data recieved!'
socket.close()
