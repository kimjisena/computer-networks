#! /usr/bin/python

from socket import socket, AF_INET, SOCK_STREAM
import sys

def client (host: str, port: int, filename: str) -> str:
  # prep the socket
  sock = socket(AF_INET, SOCK_STREAM)
  sock.connect((host, port))

  # send request headers
  headers = [
    f"GET /{filename} HTTP/1.1\r\n",
    f"Host: {host}:{str(port)}\r\n",
    "User-Agent: Python/3.11\r\n",
    "Accept: text/html\r\n",
    "Connection: keep-alive\r\n"
  ]

  for i in range(0, len(headers)):
    sock.send(headers[i].encode())
  sock.send("\r\n".encode())
  res = sock.recv(2048).decode()
  status = res.split('\r\n')[0]
  sock.close()
  return status

if __name__ == 'main':
  args = sys.argv[1:]
  client(args[0], int(args[1]), args[2])
