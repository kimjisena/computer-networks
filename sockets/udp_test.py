import unittest
from udpclient import client

class UDPTestCase (unittest.TestCase):
  def testServer(self):
    self.assertEqual(client('hello world'), 'HELLO WORLD')

if __name__ == 'main':
  unittest.main()
  