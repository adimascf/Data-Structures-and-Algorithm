def bfs_implementation(start_node, graph, end_node=None):
    """Find the of from adjacency list graph using BFS"""

    path = []
    marked = {i: False for i in range(len(graph))}
    d = 0
    queue = [(start_node, d)]

    while queue:
        v = queue.pop(0)
        if not marked[v[0]]:
            path.append((v))
            marked[v[0]] = True
            d += 1
            for w in graph[v[0]]:
                queue.append((w, d))
    return path


graph_test = {0: [1], 2: [4], 1: [3, 4], 3: [2], 4: []}

print(bfs_implementation(0, graph_test))
