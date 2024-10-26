import math
import random
import string
import numpy as np


def numberRepresentation(string: str) -> list:
    "Returns an array of numbers translated to their ASCII numerical value --> in order"
    values = []
    i = 0;
    while i < len(string):
        values.append(int(ord(string[i])));
        i += 1;
    return values
        

def codeGeneration(size: int, chars=string.digits) -> str:
    "This bad boy is courtesy of our lord and savior; Stack Overflow"
    return ''.join(random.choice(chars) for x in range(size))


def makeMessageInKeys (message: list, keys: list, charToKeys: list) -> list:
    "takes the entire message and the set of keys, and replaces every character with its corresponding keys"
    i = 0
    while i < len(keys):
        b = 0
        counter = 1
        while b < len(message):
            if (message[b] == charToKeys[i]):
                message[b] = keys[i];
                message[b] = str(counter)
                counter +=1
            b+=1
        i+=1
    return message


def encryptMessage (wholeMessageInKeys: list) -> list:
    "encrypts the entire message, this is the last stage"
    i = 0
    newMessage = []
    while i < len(wholeMessageInKeys):
        newMessage.append(encryptCharacter(wholeMessageInKeys, i))
        i+=1
    return newMessage


def encryptCharacter(messageInKeys: list, i: int) -> int:
    "takes the array of encryption keys, and returns the [i] key, and encrypts a single character"
    storage = 0 
    x = int(messageInKeys[i][0]) + int(messageInKeys[i][1])
    a = int(messageInKeys[i][2])
    b = int(messageInKeys[i][3])
    c = int(messageInKeys[i][4])
    keyIterations = int(messageInKeys[i][5])
    print(x,a,b,c)
    i = 0
    while i <= keyIterations:
        storage += math.sin( x^2 *a) + (x^b - x^c)# series sin( x^2 *a) + (x^b - x^c)
        i += 1
    encryptedCharacter = int(storage)
    return encryptedCharacter


def removeDuplicates (string: list) -> list:
    "removes all duplicates, and produces an array including all characters utilized in this message"
    return list(set(string))


def attributeParameters (usedCharacters: list) -> list:
    """**Returns as strings**  Give each letter a set of numerical parameters which will define its unique iterative series PER CHARACTER
     --> These values will be the "key" used to encrypt, and later decrypt, the message [currently 6 parameters employed]
    """
    i = 0
    keyValues = [] # <-- This array will store 6 digit integers, each index will be used for a different letter (I couldnt be bothered to figure out 2d arrays for python)
    #                                           ** empty spaces will just become 0's **
    while i < len(usedCharacters):
        randomCode = (codeGeneration(5)) + "0"; # create a code, the lase digit representing iteration count (restarts after 9 iterations)
        if (randomCode not in keyValues): # <-- checks and corrects for repeats 
            keyValues.append(randomCode)
            i += 1

    return keyValues


def main() -> None:

    class messageProperties:
        " v these values contain the entire message"
        inNumbers = 0;
        inPlainText = "";
        " v this is inportant information but !! DOES NOT CONTAIN ENTIRE MESSAGE !! "
        charactersInNumbers = [];
    
    message = messageProperties()
    message.inPlainText = input("enter message: ")

    class encryptionProperties:
        "This keeps track of my encryption parameters for each character and iteration count (and ASCII correspondance)"
        keys = []
        iterationCount = []
        correspondantASCII = [] # <-- this one is a bit more tentative
        wholeMessageInKeys = []
        finalMessage = []
    message.encryption =  encryptionProperties();

    # create my message properties from 
    message.inNumbers = numberRepresentation(message.inPlainText)
    message.charactersInNumbers = removeDuplicates(message.inNumbers)
    message.encryption.keys = attributeParameters(message.charactersInNumbers) # <-- Randomly generates key parameters for each character
    message.encryption.wholeMessageInKeys = makeMessageInKeys(message.inNumbers, message.encryption.keys, message.charactersInNumbers)
    
    message.encryption.FinalMessage = encryptMessage(message.encryption.wholeMessageInKeys)

    print(f"letters as numbers:  {message.inNumbers} {type(message.inNumbers)}")
    print(f"Characters utilized in this message:  {message.charactersInNumbers} {type(message.charactersInNumbers)}")
    print(f"paramaters / key values:  {message.encryption.keys} {type(message.encryption.keys)}")

    print()
    print()
    print(f"FIANALLY!! {message.encryption.FinalMessage}")
    print()
main()
