#! /usr/bin/python

from socket import socket, AF_INET, SOCK_STREAM
import sys
import threading

HOST = 'localhost'
PORT = 12000

def request_handler (sock: socket):
  conn, addr = sock.accept()
  try:
    # process request
    msg = conn.recv(2048).decode()
    print(f"{msg}")
    filename = msg.split()[1]
    fhandle = open(filename[1:])
    fcontent = fhandle.readlines()
    fhandle.close()
    # send http header line
    conn.send('HTTP/1.1 200 OK\r\n'.encode())
    conn.send('\r\n'.encode())
    # send file content line by line
    try:
      for i in range(0, len(fcontent)):
        conn.send(fcontent[i].encode())
    except ConnectionResetError:
      pass
    finally:
      conn.send('\r\n'.encode())
    # good job, now close connection
    conn.close()
  except IOError as err:
    print(err)
    # handle errors
    conn.send('HTTP/1.1 404 Not Found\r\n'.encode())
    conn.send('\r\n'.encode())
    conn.close()

def server ():
  # prep socket -  listen for connection in the main thread
  sock = socket(AF_INET, SOCK_STREAM)
  sock.bind(('', PORT))
  sock.listen(1)
  # accept connection
  while True:
    print('Ready to serve...')
    try:
      thread = threading.Thread(target=request_handler, args=(sock,))
      thread.start()
      thread.join()
    except KeyboardInterrupt:
      sock.close()
      sys.exit()

server()