def kahn(graph):
    # count of indegree nodes
    indegree = {node: 0 for node in graph}
    
    for node in graph:
        for neighbor in graph[node]:
            indegree[neighbor] += 1

    queue = []
    for node in graph:
        if indegree[node] == 0:
            queue.append(node)

    result = [ ]

    # like BFS
    while queue :
        node = queue.pop(0)
        result.append(node)

        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    
    if len(result) == len(graph):
        return result
    else:
        raise ValueError("Graph has a cicle")

graph = {
    'X': ['Y', 'Z'],
    'Y': ['A', 'B'],
    'Z': ['C'],
    'A': ['D'],
    'B': ['D'],
    'C': ['E'],
    'D': ['F'],
    'E': ['F'],
    'F': [],
}

result = kahn(graph)
print("Topological sorting order:", result)