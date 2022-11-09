#! /usr/bin/python

from socket import socket, AF_INET, SOCK_DGRAM

serverPort = 12002

def server ():
  serverSocket = socket(AF_INET, SOCK_DGRAM)
  serverSocket.bind(('', serverPort))

  print("The server is ready to receive...")
  while True:
    try:
      message, clientAddress = serverSocket.recvfrom(2048)
      print(f"Received request from {clientAddress}")
      modifiedMessage = message.decode().upper()
      serverSocket.sendto(modifiedMessage.encode(), clientAddress)
    except KeyboardInterrupt:
      print("Shutting down server...")
      break

server()
