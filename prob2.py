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
    while len(queue) > 0:  # queue is not empty could also say while True ?
        curr = queue[0]
        queue.pop(0)
        for elem in d:
            next = delta(curr, elem, k)
            if next == 0:
                break
            elif not visited[next]:  # state is false or not visted

                visited[next] = True
                parent[next] = curr
                label[next] = elem
                queue.append(next)
    for i in parent:
        if i == 26147:
            print('found')
    print(parent)
    print(label)
    if next != 0:
        print("No solution")
    else:
        trace(parent, label, k)


# def trace(parent, label, key):
#     length = 0
#     tempParent = parent[0]
#     solution = label[0]
#     while tempParent != key:
#         length += 1
#         solution += label[tempParent] * 10 ** length
#         tempParent = parent[tempParent]


def trace(parent, label, k):
    parentValue = parent[0]
    solution = str(label[0])
    while(parentValue != k):
        solution += str(label[parentValue])
        parentValue = parent[parentValue]
    return solution


def main():
    k = 198217
    d = [1]
    Findstring(k, d)



main()
