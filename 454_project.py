#   Assigment: 454 Project 1 Spring 2020
#   Authors: Alexander Barajas-Ritchie, Welinton De Leon, Alondra Lona
#
#
import itertools

#
# PROBLEM 1 FUNCTIONS
#
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

#
# PROBLEM 2 FUNCTIONS
#

def bfs(visited, graph, node):
    q = []
    visited.append(node)
    q.append(node)
    while q:
        s = q.pop(0)
        print(s, end=" ")

        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                q.append(neighbour)


def delta(curr, ele, k):
    return (10 * curr + ele) % k

def Findstring(k, d):

    queue = []  # initialize a queue
    parent = [0] * (k + 1)
    label = [0] * (k + 1)
    visited = [False] * (k + 1)  # array of visited states, all false
    visited[k] = True
    queue.append(k)  # added the the last element to the queue
    while queue:  # queue is not empty could also say while True ?
        curr = queue[0]
        queue.pop(0)
        done = 0
        for elem in d:
            next = delta(curr, elem, k)
            if next == 0:
                done = 1
                visited[next] = True
                parent[next] = curr
                label[next] = elem
                queue.append(next)
                break

            elif not visited[next]:  # state is false or not visted

                visited[next] = True
                parent[next] = curr
                label[next] = elem
                queue.append(next)
        if done == 1:
            break
    if next != 0:
        print("No solution")
    else:
        temp = trace(parent, label, k)
        print(temp[len(temp)::-1])

def trace(parent, label, k):
    parentValue = parent[0]
    solution = str(label[0])
    while(parentValue != k):
        solution += str(label[parentValue])
        parentValue = parent[parentValue]
    return solution

#
# MAIN
#
def main():
    # User Input for what problem they would like to work on
    print("Enter 1 for Problem 1")
    print("Enter 2 for Problem 2")
    print("Enter 0 to Quit")
    prob = int(input("Problem 1 or Problem 2? (Enter 0 to quit): "))
    while(prob != 0):
        #
        # Problem 1 Main
        #
        if (prob == 1):
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
        #
        # Problem 2 Main
        #
        elif (prob == 2):
            k = int(input("Insert a value K: "))
            print("Enter integers in the language d ( same line ):  \n > ", end='')
            d = list(map(int, input().split()))
            Findstring(k, d)
            #question = input("Quit? y/n: ")

        prob = int(input("\nEnter number for which problem you would like to do (Enter 0 to quit): "))


main()
