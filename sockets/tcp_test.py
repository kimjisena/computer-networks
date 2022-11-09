import unittest
from tcpclient import client

class TCPTestCase (unittest.TestCase):
  def testServer(self):
    self.assertEqual(client('hello world'), 'HELLO WORLD')

if __name__ == 'main':
  unittest.main()