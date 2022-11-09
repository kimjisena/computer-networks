#! /usr/bin/python

from socket import socket, AF_INET, SOCK_STREAM
import sys

HOST = 'localhost'
PORT = 12001

def server ():
  # prep socket
  sock = socket(AF_INET, SOCK_STREAM)
  sock.bind(('', PORT))
  sock.listen(1)

  # accept connection
  while True:
    print('Ready to serve...')
    conn, addr = sock.accept()
    try:
      # process request
      msg = conn.recv(2048).decode()
      print(f"{msg}")
      filename = msg.split()[1]
      fhandle = open(filename[1:])
      fcontent = fhandle.readlines()
      # send http header line
      conn.send('HTTP/1.1 200 OK\r\n'.encode())
      conn.send('\r\n'.encode())
      # send file content line by line
      for i in range(0, len(fcontent)):
        conn.send(fcontent[i].encode())
      conn.send('\r\n'.encode())
      # good job, now close connection
      conn.close()
    except IOError as err:
      print(err)
      # handle errors
      conn.send('HTTP/1.1 404 Not Found\r\n'.encode())
      conn.send('\r\n'.encode())
      conn.close()
    finally:
      pass
      #sock.close()
      #sys.exit()

server()
