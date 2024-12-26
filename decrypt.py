import math


def askiiToInt (digit: str) -> str:
    return int(ord(str(digit)))


def buildExpectedChars(keys):
    output = []
    for chars in keys:
        storage = 0 
        x = askiiToInt(chars[0]) - askiiToInt(chars[1]) + askiiToInt(chars[6])
        a = askiiToInt(chars[2]);         b = askiiToInt(chars[3]);         c = askiiToInt(chars[4]);
        keyIterations = int(int(chars[6]) / 2) + 1
        for i in range(keyIterations):
            storage += math.sin( x**2 * math.factorial(a)) + (x**b - x**c)
        output.append(int(storage))
    return output




def main():
    decrypted = "" 

    file = open("messageAndKeys.txt","r")
    message = file.readline().strip("\n").split("%")
    keys = file.readline().strip("\n").split("%")
    charMap = file.readline().strip("\n").split("%")
    print(str(message) + "\n" + str(keys) + "\n" + str(charMap))
    for i in range(len(keys)):
        keys[i] = keys[i]+'1'

    expected = buildExpectedChars(keys)
    print(str(expected))

    for chars in range(len(message)):
        for i in range(len(expected)):
            if str(expected[i]) == message[chars]:
                decrypted = decrypted +(chr(int(charMap[i])))
                keys[i] = keys[i][:-1] + str(int(keys[i][-1])+1)
                expected = buildExpectedChars(keys)

    print(F"\n{decrypted}\n")


main()