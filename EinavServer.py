from socket import *
from Queue import Queue
from thread import start_new_thread
from ServerInputThread import ClientIO

server = socket(AF_INET, SOCK_STREAM) # start server
server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1) # prevent OS from remembering the port number
print "Server On Line"

clients = {}
request_queue = Queue(0)

def output():
    '''
    messageInfo is a list of strings containing the info conveyed by the client.
    the info has the following format:
    messageInfo[0] is the client's name.
    messageInfo[1] is the data sent to the server.
    messageInfo[2] is the recipient of the data.
    if the recipient starts with a '0000' string, it is meant to reach the server and give it instructions:
        00000000:
            echo the data sent
        00000001:
            change the client's name to messageInfo[1]
        00000002:
            request a list of the connected clients and their names
    :return: None
    '''
    message = request_queue.get()
    messageInfo = message.split('::')
    sender = messageInfo[0]
    content = messageInfo[1]
    recipient = messageInfo[2].replace('\n', '')
    if recipient.startswith('0000'):
        server_output(sender, content, recipient)
    elif clients.has_key(recipient):
        clients.get(recipient).send(sender + ' said:\t' + content)
    else:
        client.send('The user does not exist')

def server_output(sender, content, recipient):
    client = clients[sender]
    if recipient.endswith('0'):
        client.send('You said: ' + content)
    elif recipient.endswith('1'):
        client = clients[sender]
        clients.pop(sender)
        clients[content] = client
        client.send('Your name has been updated!')
    elif recipient.endswith('2'):
        clientList = ''
        for key in clients.keys():
            clientList += key + '\n'
        client.send(clientList)

start_new_thread(output, ())

try:
    server.bind(('', 4444))
except Exception, e:
    server.close()
    raise e

server.listen(2)
i = 0
while True:
    client = ClientIO(server.accept()[0], request_queue)
    client.start()
    client.send(str(i)) # make sure that the client receives the message as soon as he connects.
    clients[str(i)] = client
    i += 1

