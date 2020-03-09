#   Assigment: 454 Project 1 Spring 2020
#   Authors: Alexander Barajas-Ritchie, Wellinton De Leon, Alondra Lona
#   
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



def main():
    prog = True
    while prog:
        k = int(input("Insert a value K: "))
        print("Enter integers in the language d ( same line ):  \n > ", end='')
        d = list(map(int, input().split()))
        Findstring(k, d)
        question = input("Quit? y/n: ")
        if question == "y":
            prog = False


main()
