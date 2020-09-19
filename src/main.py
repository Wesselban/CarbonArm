import importdata
import binascii

if __name__ == '__main__':
    filename = "001_Take_001"
    importdata.ConvertCMPtoTXT(filename + ".cmp")
    importdata.test(filename + ".txt", filename +"DECODED.txt" )
    