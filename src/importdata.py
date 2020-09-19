import struct
import functools
 
def splitstringLine(inputString):
    return False

def splitstringValue(inputString):
    temp =(struct.unpack('<i', inputString))
    return functools.reduce(lambda sub, ele: sub * 10 + ele,temp)
