import math
import random
import string

"""
This code is meant to take a message, generate keys, and encrypt using these keys. In a final product a new key would not be created for every message, 
rather a key would be created at the initialization of a text-room, and this key would be utilized for message encryption / decryption for the duration of the conversation.

The idea is that, so long as both users contain this key, all that needs to be sent it the last array (fully encrypted message); which will be 
reconstructed on the receiving end into a full message;
"""

"""
Issues still relevant:
    - series collisions
"""

def download(input: list) -> None:
    data = input.read()
    filename = "Encryption_Key_&_Map.txt"
    file_ = open(filename, 'w')
    file_.write(data)
    file_.close()

def askiiToInt (digit: str) -> str:
    return int(ord(str(digit)))


def numberRepresentation(string: str) -> list:
    "Returns an array of numbers translated to their numerical value --> in order"
    values = []
    i = 0;
    while (i < len(string)):
        values.append(int(ord(string[i])));
        i += 1;
    return values
        

def codeGeneration(size: int, chars=string.digits + string.ascii_lowercase + string.ascii_uppercase) -> str:
    return ''.join(random.choice(chars) for x in range(size))


def addValueToEndOfKey (keyAtIndexi: str, value: int) -> str:
    sumOf = int(keyAtIndexi[5]) + value
    keyAtIndexi[:-1]
    return str(keyAtIndexi + str(sumOf))


def makeMessageInKeys (message: list, keys: list, charToKeys: list) -> list: # string
    "takes the entire message and the set of keys, and replaces every character with its corresponding keys"
    i = 0
    while (i < len(keys)):
        b = 0
        counter = 1
        while (b < len(message)):
            if (message[b] == charToKeys[i]):
                message[b] = addValueToEndOfKey(keys[i],counter)
                if (counter < 9):
                    counter +=1
                else: 
                    counter = 0
            b+=1
        i+=1
    return message


def encryptMessage(wholeMessageInKeys: list) -> list:
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
    x = askiiToInt(messageInKeys[i][0]) - askiiToInt(messageInKeys[i][1]) + askiiToInt(messageInKeys[i][6])
    a = askiiToInt(messageInKeys[i][2])
    b = askiiToInt(messageInKeys[i][3])
    c = askiiToInt(messageInKeys[i][4])
    keyIterations = int(messageInKeys[i][6]) / 2
    i = 0
    while i <= keyIterations:
        storage += math.sin( x**2 * math.factorial(a)) + (x**b - x**c)# series sin( x^2 *a!) + (x^b - x^c) where a = uses/2 and x = x + uses *uses resets after 9*
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
    nl = "\n"
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
        keys = [] # str array
        iterationCount = [] # int array
        wholeMessageInKeys = []# str array
        finalMessage = [] # int array
    message.encryption =  encryptionProperties();

    message.inNumbers = numberRepresentation(message.inPlainText)
    print(f"{nl}message.inNumbers: {message.inNumbers} <- this array contains the entire message, with each character translated to a number. EX: a = 108 for all a's{nl}")
    message.charactersInNumbers = removeDuplicates(message.inNumbers)
    print(f"message.charactersInNumbers: {message.charactersInNumbers} <- this array contains the number-representaion of each utilized character - repititions have been removed{nl}")
  
    message.encryption.keys = attributeParameters(message.charactersInNumbers) # <-- Randomly generates key parameters for each character
    print(f"message.encryption.keys: {message.encryption.keys} <- this array contains the randomly generated key for each character (no repititions here either){nl}(last digit is the iterateion-use counter){nl}")
    message.encryption.wholeMessageInKeys = makeMessageInKeys(message.inNumbers, message.encryption.keys, message.charactersInNumbers)
    print(f"message.encryption.wholeMessageInKeys { message.encryption.wholeMessageInKeys} <- this is the original message recunstructed in terms of keys{nl}(with iteration counts computed and encoded in the last digit){nl}")
    
    message.encryption.finalMessage = encryptMessage(message.encryption.wholeMessageInKeys)
    print(f"{nl}FIANALLY!! {message.encryption.finalMessage} <- this is the message fully encrypted. This is the information that would actually be sent, and later reconstructed into the full message{nl}These values are arrived at by using the key values as parameters for an iterative series, using the last digit to increase iteration (and decrease x value) with each utilization (refer to screen-shot){nl}")
    download(message.encryption.finalMessage)
main()
