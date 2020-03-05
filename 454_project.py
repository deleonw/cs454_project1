"""
CS 454 Project 01
"""
import itertools

def isAccepted(p):
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

def numOfAccepted(size, language,count, states, holder):
    for n in range(1, size+1):
        if n < 6:
            holder.clear()
            for i in states:
                holder.append(i)
            states.clear()
            for string in holder:
                for character in language:
                    temp = string+character
                    states.append(temp)
                    if n == size:
                        count += 1
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
                        if n == size:
                            count += 1
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
                        if n == size:
                            count += 1
                        states.append(temp)
                    temp = temp[0:len(temp)-1]
            #holder.clear()
        holder.clear()

    #print(str(states))
    holder.clear()
    #print(len(states))
    states.clear()
    #print(count)
    return count

def recursiveNumAccepted(size, language, count, states, holder):
    # Recursive alternative for the function above
    if size == 0:
        return count


def main():
    size = int(input("Size of string (Enter 0 to quit): "))
    while size != 0:
        count = 0
        language = ['a', 'b', 'c', 'd']
        states = ['']
        holder = []
        answer = numOfAccepted(size, language, count, states, holder)
        print(answer)
        size = int(input("\nSize of string (Enter 0 to quit): "))

#main()

def test():
    ins = str(input('Input: '))
    while(ins != 'q'):
        toCalculate = []
        position = 0
        for letter in ins:
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
        print(position)
        ins = str(input('Input: '))

test()








