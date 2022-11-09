from socket import socket, AF_INET, SOCK_DGRAM

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))

print("The server is ready to receive...")
while True:
  message, clientAddress = serverSocket.recvfrom(2048)
  print(f"Received request from {clientAddress}")
  modifiedMessage = message.decode().upper()
  serverSocket.sendto(modifiedMessage.encode(), clientAddress)
