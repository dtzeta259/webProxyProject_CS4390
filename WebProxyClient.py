import socket

#Variables for Client socket
PORT = 65003
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

#Create the client socket and send connection request to server
clientTCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientTCP.connect(ADDR)

msg = clientTCP.recv(1024)
print(msg.decode())