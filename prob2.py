
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
    visited = [k+1]
    visited[j] = False
    visited[k] = True

    q.append(k)
    while len(q) > 0: # queue is not empty could also say while True ?
        curr = q.pop(0)
        # for each symbol c in R do:

        #   next = delta(curr,c, k); // Recall delta(q, r, k) = (10×q+r)%k.
        next = (10*curr+q) % k

        # reached an accpeting state
        if next == 0:
            break
        elif not visited[next]:
            visited[next] = True
            parent[next] = curr
            q.insert(next, 1)
    if next !=0:
        print("No solution")




