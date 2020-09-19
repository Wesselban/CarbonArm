import unittest
from importdata import splitstringLine, splitstringValue
 
 
class HelloworldTests(unittest.TestCase):
    def test_getLine(self):
        self.assertEqual(splitstringLine(''), False)
    def test_getValue(self):
        self.assertEqual(splitstringValue(b"\x03\x00\x00\x00"), 3)