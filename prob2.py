
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
    return (10 * curr + ele) % k

def Findstring(k, d,):
    queue = []
    parent = []
    label = []
    visted = [0] * (k+1)
    visted[k] = 1
    queue.append(k)
    while len(queue) > 0: # queue is not empty could also say while True ?
        curr = queue.pop()
        for elem in d:
            next = delta(curr, elem, k)
            if next == 0:
                break
            elif visted[next] == 0:
                visted[next] = True
                parent.append(curr)
                label.append(elem)
                queue.insert(next, 1)
    # if next != 0:
    #             print("No solution")
    else:
        for i in reversed(parent):
            print(i)
            # samll change

def main():
    k = 26147
    d = [1, 3]
    Findstring(k, d)

main()