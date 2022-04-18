#Computer will act as the client and this file will be the proxy that will connect to the server
#Meaning there will not be a client file for this one. However, TCP will be implemented by first
#Taking the client's arguments and then use the browser to connect to the websites

from email import parser
import socket 
import threading
import argparse
import re

#Variables for TCP sockets
BUFFER_SIZE = 6144
PORT = 65003 #The port that will be used for the project
SERVER = socket.gethostbyname(socket.gethostname())
SERVER_ADDR = (SERVER, PORT)

#Read in the arguments for the server ip and port, if any
#otherwise, use the default port and server ip.

parser = argparse.ArgumentParser(description="HTTP proxy server project.")

parser.add_argument("serverIP", nargs="?", default= SERVER, 
                    help="Address for the proxy server to listen on. Default is 192.168.1.86")

parser.add_argument("serverPort", nargs="?", type=int, default=PORT, 
                    help="Port for binding the listening socket to. Default is 65003")

argServer = parser.parse_args()

#Methods for the proxy server

def requestsGET(clientSock, address):
    print("Message Received from Client {}:\n" .format(address))
    
    clientMessage = clientSock.recv(BUFFER_SIZE).decode()
    
    #Parse the HTTP request and print it out
    getRequest = clientMessage.split()

#Create proxy server socket and listen for get requests
serverTCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverTCP.bind(SERVER_ADDR)
serverTCP.listen(5)
print("HTTP Proxy Server is listening on IP and port: {}:{}" .format(argServer.serverIP, argServer.serverPort))

#Connection is established, begin serving via threading
while True:
    clientSocket, address = serverTCP.accept()
    print("Connection from {} established! Begin client communication." .format(address))
    threading.Thread(target=requestsGET, args=(clientSocket, address))
    

