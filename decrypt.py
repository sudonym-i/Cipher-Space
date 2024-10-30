import math
import random
import string

def askiiToInt (digit: str) -> str:
    return int(ord(str(digit)))

def parseArrayInChunks (messageKeys):
    finalArray = []
    tempString = ""
    i = 1
    while i < messageKeys:
        tempString.append(messageKeys[i-1])
        if (i % 6 == 0):
            finalArray.append(tempString)
            tempString = ""
    return finalArray
        

def encryptCharacter(charInKeys: list, i: int) -> int:
    "takes the array of encryption keys, and returns the [i] key, and encrypts a single character"
    storage = 0 
    x = askiiToInt(charInKeys[i][0]) - askiiToInt(charInKeys[i][1]) + askiiToInt(charInKeys[i][6])
    a = askiiToInt(charInKeys[i][2])
    b = askiiToInt(charInKeys[i][3])
    c = askiiToInt(charInKeys[i][4])
    keyIterations = int(charInKeys[i][6]) / 2
    i = 0
    while i <= keyIterations:
        storage += math.sin( x**2 * math.factorial(a)) + (x**b - x**c)# series sin( x^2 *a!) + (x^b - x^c) where a = uses/2 and x = x + uses *uses resets after 9*
        i += 1
    encryptedCharacter = int(storage)
    return encryptedCharacter

def buildExpectedCharacters(messageKeys) -> list:
    i = 0
    expectedChars = []
    while i < len(messageKeys):
        expectedChars.append(encryptCharacter(messageKeys, i));
        i += 1
    return expectedChars

def main () -> None:
    nl = "\n"
    class messageProperties:
        " v these values contain the entire message"
        inNumbers = 0;
        inPlainText = "";
        " v this is inportant information but !! DOES NOT CONTAIN ENTIRE MESSAGE !! "
        charactersInNumbers = [];
    message = messageProperties()

    class encryptionProperties:
        "This keeps track of my encryption parameters for each character and iteration count (and ASCII correspondance)"
        keys = [] # str array
        iterationCount = [] # int array
        wholeMessageInKeys = []# str array
        finalMessage = [] # int array
    message.encryption =  encryptionProperties();

    message.encryption.keys = parseArrayInChunks((input("copy-paste the encryption keys (NOT the one titled 'whole message in keys'): ")))
    message.charactersInNumbers = list(input(f"copy-paste 'characters in numbers'"))
    message.encryption.finalMessage = list(input(f"{nl}copy-paste the fully encrypted message: ")) # <- this is the only 
    # information that would actually be transmitted; the rest would be part of the 'conversation setup'
    
    print(buildExpectedCharacters(message.encryption.keys))

main()