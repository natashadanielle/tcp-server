#! /usr/bin/python3

import socket

#Creating the socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#host = '192.168.1.104'
host = socket.gethostname()
port = 444

#Binding to socket 
serversocket.bind('192.168.1.104', port)

#StartingTCP listener
serversocket.listen(3)

while True:
    #Starting the connection
    clientsocket, address = serversocket.accept()

    print("received connection from %s " % str(address))

    message = 'Thank you for connecting to the server' + "\r\n"
    
    clientsocket.send(message.encode('ascii'))

    clientsocket.close()
