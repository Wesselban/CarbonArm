import unittest
import importdata
 
 
class importdatatests(unittest.TestCase):
    def test_getLine(self):
        self.assertEqual(importdata.splitstringLine(''), False)
    def test_getValue(self):
        self.assertEqual(importdata.splitstringValue(b"\x03\x00\x00\x00"), 3)
    def test_convertCMPtoTXTNoFile(self):
        self.assertEqual(importdata.ConvertCMPtoTXT(""), False)
    def test_convertCMPtoTXTNoCMPFile(self):
        self.assertEqual(importdata.ConvertCMPtoTXT("test.txt"), False)
    def test_convertCMPtoTXTNonExistingFile(self):
        self.assertEqual(importdata.ConvertCMPtoTXT("testnonexisting.cmp"), False)
    def test_convertCMPtoTXT(self):
        self.assertEqual(importdata.ConvertCMPtoTXT("test.cmp"), "test.txt")
    def test_convertTXTtoCMPNoFile(self):
        self.assertEqual(importdata.ConvertTXTtoCMP(""), False)
    def test_convertTXTtoCMPNTXTFile(self):
        self.assertEqual(importdata.ConvertTXTtoCMP("test.cmp"), False)
    def test_ConvertTXTtoCMPNonExistingFile(self):
        self.assertEqual(importdata.ConvertTXTtoCMP("testnonexisting.txt"), False)
    def test_ConvertTXTtoCMP(self):
        self.assertEqual(importdata.ConvertTXTtoCMP("test2.txt"), "test2.cmp")
    