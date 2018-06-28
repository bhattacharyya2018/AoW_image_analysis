#!/usr/bin/env python

#Ayesha Rizvi TCP Server Original
from socket import *
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM) #creates socket
serverSocket.bind(('',serverPort)) #binds to port 
serverSocket.listen(1) #listens for incoming connections
print ('The server is ready to receive')
while 1:
	#with open('received_file', 'wb') as f:
        #print 'file opened'
	connectionSocket, addr = serverSocket.accept()
	#data = connectionSocket.recv(60000).decode()
        data = connectionSocket.recv(600000)
	print(data)
	#capitalizedSentence = sentence.upper()
	#connectionSocket.send(capitalizedSentence)
	connectionSocket.close()
        #serverSocket.close()
	#break 

