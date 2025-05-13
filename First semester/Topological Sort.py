def dfs(graph, vertex, stack, visited):
    visited.add(vertex)
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs(graph, neighbor, stack, visited)
    stack.append(vertex)

def topological_sort(graph):
    stack = []
    visited = set()
    for vertex in graph:
        if vertex not in visited:
            dfs(graph, vertex, stack, visited)
    ordering = []
    while stack:
        ordering.append(stack.pop())
    return ordering
graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": ["G"],
    "E": ["G", "H"],
    "F": ["I"],
    "G": ["J"],
    "H": [],
    "I": ["J"],
    "J": ["K"],
    "K": ["L"],
    "L": []
}

print(topological_sort(graph))