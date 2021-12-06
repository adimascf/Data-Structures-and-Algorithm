from queue import PriorityQueue


def djikstra_implementation(graph, start, end):
    """Find a shortest path from a given a
    weighted graph"""

    unseen_nodes = graph
    path = []
    predecesor = {}
    shortest_distance = {n: float('inf') for n in unseen_nodes}
    shortest_distance[start] = 0

    while unseen_nodes:
        min_node = None
        for node in unseen_nodes:
            if min_node is None:
                min_node = node
            elif shortest_distance[node] < shortest_distance[min_node]:
                min_node = node

        for child_node, weight in graph[min_node].items():
            if weight + shortest_distance[min_node] < shortest_distance[child_node]:
                shortest_distance[child_node] = weight + \
                    shortest_distance[min_node]
                predecesor[child_node] = min_node
        unseen_nodes.pop(min_node)

    print(shortest_distance)
    # create the path
    current_node = end
    while current_node != start:
        try:
            path += current_node
            current_node = predecesor[current_node]
        except KeyError:
            return 'Path is not reachable'
    path += start
    if shortest_distance[end] != float('inf'):
        print('Shortest ditance is ' + str(shortest_distance[end]))
        return path[::-1]


def dijkstra_pqueue(graph, start, end):

    path = []
    marked = {i: False for i in graph.keys()}
    shortest_distance = {n: float('inf') for n in graph}
    shortest_distance[start] = 0
    predecesor = {}
    pq = PriorityQueue()  # use priority queue
    pq.put((start, shortest_distance[start]))
    arr = [start]  # using array, for tracking the node (pop and append)
    while arr:
        v = pq.get()
        curr = v[0]
        arr.pop(arr.index(curr))
        for child, weight in graph[curr].items():
            if weight + shortest_distance[curr] < shortest_distance[child]:
                shortest_distance[child] = weight + \
                    shortest_distance[curr]
                pq.put((child, shortest_distance[child]))
                arr.append(child)
                predecesor[child] = curr

    print(shortest_distance)
    # create the path
    current_node = end
    while current_node != start:
        try:
            path += current_node
            current_node = predecesor[current_node]
        except KeyError:
            return 'Path is not reachable'
    path += start
    if shortest_distance[end] != float('inf'):
        print('Shortest ditance is ' + str(shortest_distance[end]))
        return path[::-1]


graph_test = {'a': {'b': 1, 'c': 6, 'd': 3}, 'b': {'c': 4},
              'c': {}, 'd': {'c': 1}}

print('Priority queue')
print(dijkstra_pqueue(graph_test, 'a', 'c'))
print('\nNon-priority queue')
print(djikstra_implementation(graph_test, 'a', 'c'))
