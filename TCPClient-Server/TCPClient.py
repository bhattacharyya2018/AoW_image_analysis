#!/usr/bin/env python

#Ayesha Rizvi TCP Client Original
from socket import *
serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM) #creates socket
clientSocket.connect((serverName,serverPort)) #connects to server
file = open("numpyarray2.txt")
l = file.read()
while 1:
  #sentence = raw_input('Input lowercase sentence:')
   clientSocket.send(l)
   print("Done Sending")
   file.close()
   clientSocket.close()
   break
