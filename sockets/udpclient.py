from socket import socket, AF_INET, SOCK_DGRAM
import sys

serverName = 'localhost'
serverPort = 12002

def client(message: str) -> str:
  clientSocket = socket(AF_INET, SOCK_DGRAM)
  clientSocket.sendto(message.encode(), (serverName, serverPort))
  modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
  clientSocket.close()
  return modifiedMessage.decode()

if __name__ == 'main':
  client(sys.argv[1])
