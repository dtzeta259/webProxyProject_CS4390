#Computer will act as the client and this file will be the proxy that will connect to the server
#Meaning there will not be a client file for this one. However, TCP will be implemented by first
#Taking the client's arguments and then use the browser to connect to the websites

from email import parser
import socket 
import argparse

#Variables for TCP sockets
PORT = 5005 #The port that will be used for the project
BUFFER = 4096
SERVER = "localhost"
SERVER_ADDR = (SERVER, PORT)

#Variables for Caching
header_mp = {}
file_mp = {}
message_mp = {}

#Read in the arguments for the server ip and port, if any
#otherwise, use the default port and server ip.

parser = argparse.ArgumentParser(description="HTTP proxy server project.")

parser.add_argument("serverIP", nargs="?", default= SERVER, 
                    help="Address for the proxy server to listen on. Default is 192.168.1.86")

parser.add_argument("serverPort", nargs="?", type=int, default=PORT, 
                    help="Port for binding the listening socket to. Default is 65003")

argServer = parser.parse_args()

#Create proxy server socket and listen for get requests
serverTCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverTCP.bind(SERVER_ADDR)
serverTCP.listen(5)
print("HTTP Proxy Server is listening on IP and port: {}:{}" .format(argServer.serverIP, argServer.serverPort))

#Methods for parsing responses
#Parse response data method
def get_header(response):
	res = response
	res = res.split('\r\n\r\n')[0]
	return res
#Parse for the method, destination address, and http version
def parse_data(response):
	#return method, destAddr, http version
	cur = ""
	lst = []
	for i in range(len(response)):
		char = response[i]
		if (char == '\r' or char == '\n'):
			lst.append(cur)
			break
		elif (char == ' '):
			lst.append(cur)
			cur = ""
		else:
			cur += char
	return lst[0] , lst[1][1:] , lst[2]

#Parse method for the host, url, and filename
def parse_link(link):
	#need to get host , url , filename
	host = ""
	for i in range(len(link)):
		if (link[i] == str('/')[0]):
			break
		host += link[i]
		
	filename = ""
	for i in range(len(link)):
		if (link[i] == str('/')[0]):
			filename = ""
		filename += link[i]
		
	url = link[len(host) :]
	
	if (str(filename) == str(host)):
		filename = "/"
	
	if(host == ""):
		print("")
	else:
		print("\n[PARSE REQUEST HEADER] HOSTNAME IS", host,'\n')
  
	if(url == ""):
		print("")
	else:
		print('[PARSE REQUEST HEADER] URL IS ',url[1:],'\n')
  
	if(filename == "/"):
			print("")
	else:
		print('[PARSE REQUEST HEADER] FILENAME IS ',filename[1:],'\n')
  
	return host , url[1:] , filename[2:]

while True:
	clientSocket, address = serverTCP.accept()
	print("Connection from {} established! Begin client communication." .format(address))
	data = clientSocket.recv(BUFFER)
	data = str(data.decode("utf-8"))

	method, link, version = parse_data(data)
	if (str(link) == str("favicon.ico")):
		continue
	print("MESSAGE RECEIVED FROM CLIENT:")
	print(data)
	print("")
	print("END OF MESSAGE RECEIVED FROM CLIENT")
	print("")
	print("[PARSE MESSAGE HEADER]")

	print(' METHOD = ',method,' DESTADDRESS = ',link,' HTTPVersion = ',version)
 
	print(file_mp.keys())

	if (link not in file_mp.keys()):
		print("[LOOK UP IN THE CACHE]: NOT FOUND, BUILD REQUEST TO SEND TO ORIGINAL SERVER")


		target_port = 80  # create a socket object 
		client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
	
		#create a socket and send request to sever
		target_host, obj , filename = parse_link(link)	

		#send some data 
		print("REQUEST MESSAGE SENT TO ORIGINAL SERVER")
		request = "GET /" +obj+" HTTP/1.1\r\nHost: " + target_host+"\r\n"
		request += "Connection: close\r\n"
		request += "Upgrade-Insecure-Requests: 1\r\n"
		request += "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36\r\n"
		request += "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n"
		request += "Sec-Fetch-Site: none\r\n"
		request += "Sec-Fetch-Mode: navigate\r\n"
		request += "Accept-Encoding: gzip, deflate, br\r\n"
		request += "Accept-Language: en-US,en;q=0.9,fr;q=0.8,vi;q=0.7\r\n"
		request += "\r\n"
		
		# connect the client 
		print(request + "\n")

		print("END OF MESSAGE SENT TO ORIGINAL SERVER")
		client.connect((target_host,target_port))  
		client.send(request.encode())
		
		print("\n\nRESPONSE HEADER FROM ORIGINAL SERVER:")
		res = client.recv(BUFFER)
		header_sv = get_header(str(res.decode("utf-8")))
		print(header_sv)

		print("END OF HEADER\n\n")
		
		print("RESPONSE HEADER FROM PROXY TO CLIENT:")
		print(header_sv)
		clientSocket.send(res)
		print("END OF HEADER")
		if(filename != "/"):
			print("\n\n[WRITE FILE INTO CACHE]: cache/",filename)
			header_mp[link] = header_sv
			file_mp[link] = "cache/"+filename
			message_mp[link] = res
			
		client.close()
		clientSocket.close()
	else:
		print("[LOOK UP IN THE CACHE]: FOUND IN THE CACHE: FILE =",file_mp[link])
		res = message_mp[link]
		header_sv = header_mp[link]
		print("RESPONSE HEADER FROM PROXY TO CLIENT:")
		print(header_sv)
		clientSocket.send(res)
		clientSocket.close()
		print("END OF HEADER")
	
	
	serverTCP.close()
	break