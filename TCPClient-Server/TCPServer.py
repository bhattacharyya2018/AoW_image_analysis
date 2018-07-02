#!/usr/bin/env python

#Ayesha Rizvi TCP Server Original
from socket import *
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM) #creates socket
serverSocket.bind(('',serverPort)) #binds to port 
serverSocket.listen(1) #listens for incoming connections
print ('The server is ready')
#file = open("numpyarray2.txt")
file = open("/root/Tcp/tiffimages/AgBH_capillary_det5m_36.2s_x-36.520_y-2.370_5.00s_13219_saxs.tiff")
l = file.read()
while 1:
	#with open('received_file', 'wb') as f:
        #print 'file opened'
	connectionSocket, addr = serverSocket.accept()
	#data = connectionSocket.recv(60000).decode()
        #data = connectionSocket.recv(600000)
	connectionSocket.send(l)
	#print(data)
	#capitalizedSentence = sentence.upper()
	#connectionSocket.send(capitalizedSentence)
	connectionSocket.close()
        #serverSocket.close()
	#break 
