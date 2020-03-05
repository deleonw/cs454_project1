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

def recursiveNumAccepted(size, language, states, holder):
    # NFA SetUp
    # Dictionary
    #   {
    #   State # : { 'a' : state #, 'b' : state #, 'c' : state #, 'd' : state #},
    #   State # : { 'aa' : state #, 'ab' : state #, 'ac' : state #, 'ad' : state #},
    #   ...
    #
    #   }
    nfa = dict()

    # change variable below later
    for i in range(0, size):
        accepted = listOfAccepted(i+1, language, states, holder)
        temp = dict()
        for j in range(0, len(accepted)):
            temp[accepted[j]] = calcPos(accepted[j])
        nfa[i] = temp
    print(str(nfa))
    print(len(nfa))

def listOfAccepted(size, language, states, holder):
    # Iterative version of finding a list of accepted states at given SIZE
    # Returns the list of accepted string
    # Takes a while to calculate for any size 13 and greater
    for n in range(1, size+1):
        if n < 6:
            holder.clear()
            for i in states:
                holder.append(i)
            states.clear()
            for string in holder:
                for character in language:
                    temp = string + character
                    states.append(temp)

                    #if n == size:
                        #count += 1
            #holder.clear()
      
        elif n == 6:
            holder.clear()
            for i in states:
                holder.append(i)
            states.clear()
            for string in holder:
                temp = string[:]
                for character in language:
                    temp = temp + character
                    if isAccepted(temp):
                        #if n == size:
                            #count += 1
                        states.append(temp)
                    temp = temp[0:len(temp) - 1]
            # holder.clear()
        else:
            holder.clear()
            for i in states:
                holder.append(i)
            states.clear()
            for string in holder:
                temp = string[1:]
                for character in language:
                    temp = temp + character
                    if isAccepted(temp):
                        #if n == size:
                            #count += 1
                        states.append(temp)
                    temp = temp[0:len(temp) - 1]
            # holder.clear()
        holder.clear()

    #print(str(states))
    #print(len(states))
    #print(count)
    return states

# Temporary
def recursiveNumAccepted(size, language,count, states, holder):
    # NFA SetUp
    # Dictionary
    #   {
    #   State # : { 'a' : state #, 'b' : state #, 'c' : state #, 'd' : state #},
    #   State # : { 'a' : state #, 'b' : state #, 'c' : state #, 'd' : state #},
    #   ...
    #
    #   }
    states = dict()


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
    for i in range(1, 6):
        for perm in itertools.product("abcd", repeat=i):
            temp = ""
            allstring.append(temp.join(perm))
    return allstring

def nextstate(string, prev, curr):
    tempA = string + 'a'
    tempB = string + 'b'
    tempC = string + 'c'
    tempD = string + 'd'
    if (len(tempA) > 5):
        tempA = tempA[1:]
    if (len(tempB) > 5):
        tempB = tempB[1:]
    if (len(tempC) > 5):
        tempC = tempC[1:]
    if (len(tempD) > 5):
        tempD = tempD[1:]

    if isAccepted(tempA):
        # curr[calcPos(tempA)]
    if isAccepted(tempB):
        # curr[calcPos(tempB)]
    if isAccepted(tempA):
        # curr[calcPos(tempC)]
    if isAccepted(tempA):
        # curr[calcPos(tempD)]


def main():
    # size = int(input("Size of string (Enter 0 to quit): "))
    # while size != 0:
    #     language = ['a', 'b', 'c', 'd']
    #     states = ['']
    #     holder = []
    #     answer = listOfAccepted(size, language, states, holder)
    #     # prints list of accepted strings
    #     print(answer)
    #     # prints the number of accepted strings
    #     print(len(answer))
    #     size = int(input("\nSize of string (Enter 0 to quit): "))

        prev = [1] * 1365
        curr = [0] * 1365

        base4 = {}
        possible = possiblestring()
        for element in possible:
            temp = calcPos(element)
            base4[temp] = element

        n = 1
        for i in range(n):
            for k, v in base4.items():  # go through prev list
                nextstate(v, prev, curr)
            # curr = prev

        print(curr)

main()

#
#
# prev = [1] * 1365
# curr = [0] * 1365



# def nextstate(index, prev, curr):
