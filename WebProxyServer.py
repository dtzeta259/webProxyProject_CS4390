from base64 import encode
import socket 
import threading

#Variables for TCP client-server sockets
PORT = 65003 #Testing Port. Cannot use Port 80 for now
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
connectMsg = "You have connected to the server. Welcome!"

#Create server socket and listen for client handshake
serverTCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverTCP.bind(ADDR)
serverTCP.listen(5)

while True:
    clientSock, address = serverTCP.accept()
    print("Connection from {} established! Begin client communication." .format(address))
    clientSock.send(connectMsg.encode())