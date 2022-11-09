#! /usr/bin/python

from socket import socket, AF_INET, SOCK_STREAM

serverPort = 12001

def server ():
  serverSocket = socket(AF_INET, SOCK_STREAM)
  serverSocket.bind(('', serverPort))
  serverSocket.listen(1)
  print(f"Server is listening on port {serverPort}")

  while True:
    try:
      connectionSocket, addr = serverSocket.accept()
      print(f"Received a request from {addr}")
      sentence = connectionSocket.recv(1024).decode()
      connectionSocket.send(sentence.upper().encode())
      connectionSocket.close()
    except KeyboardInterrupt:
      print("Shutting down server...")
      break

server()
