
def bfs (visited, graph, node):
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
    return ((10 * curr) + ele) % k

def Findstring(k, d):
    queue = [] # initialize a queue
    parent = [None] * (k+1)
    label = [None] * (k+1)
    visited = [0] * (k+1) # array of visited states, all false
    visited[k] = 1
    queue.append(k) # added the the last element to the queue
    while len(queue) > 0: # queue is not empty could also say while True ?
        curr = queue[0]
        queue.pop(0)
        for elem in d:
            next = delta(curr, elem, k)
            if next == 0:
                break
            elif visited[next] == 0: # state is false or not visted
                visited[next] = 1
                parent[next] = curr
                label[next] = elem
                queue.append(next)
    if next != 0:
            print("No solution")
    else:
        trace(parent, label)

def trace(parent, label):
    pass

def main():
    k = 26147
    d = [1, 3]
    Findstring(k, d)

main()
