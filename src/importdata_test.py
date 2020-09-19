import unittest
import importdata
 
 
class importdatatests(unittest.TestCase):
    def test_getLine(self):
        self.assertEqual(importdata.splitstringLine("83000000000000006400080700000000000000005500"), "83000000 00000000 6400 08070000 0000 00000000 5500")
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
    def test_convertTXTtoCMPNoTXTFile(self):
        self.assertEqual(importdata.ConvertTXTtoCMP("test.cmp"), False)
    def test_ConvertTXTtoCMPNonExistingFile(self):
        self.assertEqual(importdata.ConvertTXTtoCMP("testnonexisting.txt"), False)
    def test_ConvertTXTtoCMP(self):
        self.assertEqual(importdata.ConvertTXTtoCMP("test2.txt"), "test2.cmp")