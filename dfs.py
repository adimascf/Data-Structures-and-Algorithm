def dfs_implementation(start_node, graph):
    """Using DFS, find path from a given graph"""

    path = []
    marked = {i: False for i in range(len(graph))}
    stack = [start_node]

    while stack:
        v = stack.pop()
        if not marked[v]:
            path.append((v))
            marked[v] = True
            for w in graph[v]:
                stack.append(w)
    return path


graph_test = {0: [1], 2: [4], 1: [3, 4], 3: [2], 4: []}

print(dfs_implementation(0, graph_test))
