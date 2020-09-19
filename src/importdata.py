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
            outputString += "0000 "
        if i%44 == 28:
            outputString += " "
        if i%44 == 32:
            outputString += "0000 "
        if i%44 == 40:
            outputString += " "
        if i%44 == 0:
            if i != 0:
                outputString += "0000"
        outputString += inputString[i]
    outputString +="0000"
    return outputString

def splitstringValue(inputString):
    temp =(struct.unpack('<i', inputString))
    tempvalue = functools.reduce(lambda sub, ele: sub * 10 + ele,temp)
    return tempvalue


def ConvertTo62(string):
    temp = ''
    for i in range(len(string)):
            if i%62 == 0 :
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
    outputfile.write(ConvertTo62(splitstringLine(tempString)))
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

def ConvertStringToHexString(inputString):
    tempString = ""
    returnString = ""
    for i in range(len(inputString)):
        if inputString[i] == ' ':
            returnString += str(splitstringValue(ConvertHextoHexcodec(tempString))) + " "
            tempString = ""
            continue
        tempString += inputString[i]

    returnString += str(splitstringValue(ConvertHextoHexcodec(tempString)))
    return returnString

def ConvertHextoHexcodec(inputHexString):
    return binascii.unhexlify(inputHexString)
