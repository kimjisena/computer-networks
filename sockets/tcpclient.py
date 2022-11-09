from socket import socket, AF_INET, SOCK_STREAM
import sys

serverName = 'localhost'
serverPort = 12001

def client (sentence: str) -> str:
  clientSocket = socket(AF_INET, SOCK_STREAM)
  clientSocket.connect((serverName, serverPort))
  # sentence = input('Input lowecase sentence: ')
  clientSocket.send(sentence.encode())
  modifiedSentence = clientSocket.recv(1024)
  print('From Server: ', modifiedSentence.decode())
  clientSocket.close()
  return modifiedSentence.decode()

if __name__ == 'main':
  client(sys.argv[1])
