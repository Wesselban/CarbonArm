import unittest
import importdata

class importdataTests(unittest.TestCase):
    def test_getLine(self):
        self.assertEqual(importdata.splitstringLine(''), False)
    def test_getValue(self):
        self.assertEqual(importdata.splitstringValue(b"\x03\x00\x00\x00"), 3)

if __name__ == '__main__':
    unittest.main()
