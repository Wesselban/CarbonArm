import struct
import functools
import binascii
 
def splitstringLine(inputString):
    outputString = ""
    for i in range(len(inputString)):
        if i%44 == 8:
            outputString += " "
        if i%44 == 16:
            outputString += " "
        if i%44 == 20:
            outputString += " "
        if i%44 == 28:
            outputString += " "
        if i%44 == 32:
            outputString += " "
        if i%44 == 40:
            outputString += " "
        outputString += inputString[i]
    return outputString

def splitstringValue(inputString):
    temp =(struct.unpack('<i', inputString))
    return functools.reduce(lambda sub, ele: sub * 10 + ele,temp)

def ConvertTo50(string):
    temp = ''
    for i in range(len(string)):
            if i%50 == 0 :
                if i != 0:
                    temp += '\n'
            temp += string[i]

    return temp

def CheckIfValidInputFile(File):
    if not File:
        return False
    try:
        open(File, 'rb')
    except IOError:
        return False

def ConvertCMPtoTXT(cmpFile):
    if CheckIfValidInputFile(cmpFile) == False:
        return False
    if cmpFile[-4:] != ".cmp":
        return False
    with open(cmpFile, 'rb') as f:
        content = f.read()
    outputfile = open(cmpFile[0:-3]+"txt","w+")
    tempString = str(binascii.hexlify(content))[2:-1]
    outputfile.write(ConvertTo50(splitstringLine(tempString)))
    return cmpFile[0:-3]+"txt"

def ConvertTXTtoCMP(txtFile):
    if CheckIfValidInputFile(txtFile) == False:
        return False
    if txtFile[-4:] != ".txt":
        return False
    with open(txtFile, 'rb') as f:
        content = f.read()
    outputfile = open(txtFile[0:-3]+"cmp","w+")
    outputfile.write(str((binascii.unhexlify(content))[2:-1].replace(' ', '').replace('\n', '')))
    return txtFile[0:-3]+"cmp"