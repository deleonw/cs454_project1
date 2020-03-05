
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


def String(state, q, parent, visited, subsetList, k, j):
    q = []
    visited[1] * k+1
    visited[k] = True

    q.append(k)
    while len(q) > 0: # queue is not empty could also say while True ?
        curr = q.pop(0)
        # for each symbol c in R do:
        for ele in subsetList:
            #   next = delta(curr,c, k); // Recall delta(q, r, k) = (10×q+r)%k.
            next = delta(curr, ele, k)

            # reached an accpeting state
            if next == 0:
                break
            elif next not in visited:
                visited[next] = True
                parent[next] = curr
                #label[next] = c
                q.insert(next, 1)
    if next != 0:
        print("No solution")
    else:
        #trace the string using parent pointers and concatenate label symbols as you trace until start state is reached.
        # output the string.



def delta(curr, ele, k):
    return (10 * curr + ele) % k
