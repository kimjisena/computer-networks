#! /usr/bin/python

import unittest
from client import client

HOST = 'localhost'
PORT = 12001

class WebServerTestCase (unittest.TestCase):
  def testResponseOK (self):
    self.assertEqual(client(HOST, PORT, 'index.html'), 'HTTP/1.1 200 OK')

  def testResponseNotFound (self):
    self.assertEqual(client(HOST, PORT, 'about.html'), 'HTTP/1.1 404 Not Found')

if __name__ == 'main':
  unittest.main()
else:
  unittest.main()