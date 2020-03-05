"""
CS 454 Project 01
"""
import itertools


def isAccepted(p):
    # Checks if string p of size 6 is an accepted string or not
    # An accepted string is a string that contains at least one of each in {'a', 'b', 'c', 'd'}
    if(len(p) <= 5):
        return True
    foundA = foundB = foundC = foundD = False
    for i in p:
        if i == 'a':
            foundA = True
        elif i == 'b':
            foundB = True
        elif i == 'c':
            foundC = True
        elif i == 'd':
            foundD = True
    if foundA and foundB and foundC and foundD:
        return True
    return False

def calcPos(string):
    # Given a string of language {'a', 'b', 'c', 'd'} it calculates the an integer
    # which will be the State number.
    toCalculate = []
    position = 0
    for letter in string:
        toCalculate.append(letter)
    for i in range(0, len(toCalculate)):
        if toCalculate[i] == 'a':
            position = position + 1 * pow(4, (len(toCalculate) - 1) - i)
        if toCalculate[i] == 'b':
            position = position + 2 * pow(4, (len(toCalculate) - 1) - i)
        if toCalculate[i] == 'c':
            position = position + 3 * pow(4, (len(toCalculate) - 1) - i)
        if toCalculate[i] == 'd':
            position = position + 4 * pow(4, (len(toCalculate) - 1) - i)
    return position

def possiblestring():
    allstring = []
    allstring.append("")
    for i in range(1, 6):
        for perm in itertools.product("abcd", repeat=i):
            temp = ""
            allstring.append(temp.join(perm))
    return allstring

def nextstate(key, string, prev, curr):
    count = 0
    tempA = string + 'a'
    tempB = string + 'b'
    tempC = string + 'c'
    tempD = string + 'd'

    if isAccepted(tempA):
        if (len(tempA) > 5):
            tempA = tempA[1:]
        count += prev[calcPos(tempA)]

    if isAccepted(tempB):
        if (len(tempB) > 5):
            tempB = tempB[1:]
        count += prev[calcPos(tempB)]

    if isAccepted(tempC):
        if (len(tempC) > 5):
            tempC = tempC[1:]
        count += prev[calcPos(tempC)]

    if isAccepted(tempD):
        if (len(tempD) > 5):
            tempD = tempD[1:]
        count += prev[calcPos(tempD)]

    curr[key] = count


def main():
    size = int(input("Size of string (Enter 0 to quit): "))
    prev = [1] * 1365
    curr = [0] * 1365
    base4 = {}
    possible = possiblestring()
    for element in possible:
        temp = calcPos(element)
        base4[temp] = element
    for i in range(size):
        for k, v in base4.items():  # go through prev list
            nextstate(k, v, prev, curr)
        prev = curr
        curr = [0] * 1365
    print(prev[0])


main()


