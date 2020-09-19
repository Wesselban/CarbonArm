import struct
import functools
import binascii
 
def splitstringLine(inputString):
    return False

def splitstringValue(inputString):
    temp =(struct.unpack('<i', inputString))
    return functools.reduce(lambda sub, ele: sub * 10 + ele,temp)

def ConvertCMPtoTXT(cmpFile):
    if not cmpFile:
        return False
    if cmpFile[-4:] != ".cmp":
        return False
    try:
        with open(cmpFile, 'rb') as f:
            content = f.read()
    except IOError:
        return False
    outputfile = open(cmpFile[0:-3]+"txt","w+")
    outputfile.write(str(binascii.hexlify(content))[2:-1])
    return cmpFile[0:-3]+"txt"

def ConvertTXTtoCMP(txtFile):
    if not txtFile:
        return False
    if txtFile[-4:] != ".txt":
        return False
    try:
        with open(txtFile, 'rb') as f:
            content = f.read()
    except IOError:
        return False
    outputfile = open(txtFile[0:-3]+"cmp","w+")
    outputfile.write(str(binascii.unhexlify(content))[2:-1])
    return txtFile[0:-3]+"cmp"

